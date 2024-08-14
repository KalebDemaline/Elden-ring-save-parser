import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ParseService } from '../service/parse.service';

import { switchMap, tap } from 'rxjs';

//Materials
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressBarModule } from '@angular/material/progress-bar';

//Grid
import { AgGridAngular } from 'ag-grid-angular'; // Angular Data Grid Component
import { ColDef } from 'ag-grid-community'; // Column Definition Type Interface

interface rowData{
    item: string
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    //Materials
    MatToolbarModule,
    MatButtonModule,
    MatSelectModule,
    MatProgressBarModule,
    //Grid
    AgGridAngular
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {

  userId: string
  loading: boolean
  charNames: string[]
  colDefs: ColDef[]
  rowData: rowData[]

  constructor(private parseService: ParseService) {
    this.userId = ''
    this.loading = false
    this.charNames = []
    this.colDefs = [{field: "item"}]
    this.rowData = []
  }

  ngOnInit(): void {
    this.userId = this.getCookie('userID');
    if (this.userId !== "NA") {
      // existing user
      this.parseService.getCharacterInfo(this.userId, 0).subscribe(console.log)
    }
  }

  getCookie(name: string) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    let result = "NA";
    ca.forEach((c) => {
      if (c.includes(nameEQ)) {
        // If starts with space moves over 1 till characters
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        result = c.substring(nameEQ.length, c.length);
      }
    })
    return result;
  }

  setCookie(name: string, value: string, days: number) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
  }

  generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

  onFileSelected(event: any): void {
    this.loading = true
    const file: File = event.target.files[0];

    if(!file){
      return
    }

    if(this.userId === "NA"){
      let generatedId = this.generateUUID();
      this.setCookie('userID', generatedId, 365); // expires in 365 days
      this.userId = generatedId
    }

    this.parseService.sendSaveFile(this.userId, file).pipe(
      switchMap((res) => {
        if (res > 0) {
          return this.parseService.getCharacterNames(this.userId, 0)
        } else {
          throw new Error()
        }
      }),
      tap((res) => { this.charNames = res }),
      switchMap((res) => {
        if (res.length > 0) {
          return this.parseService.getCharacterInfo(this.userId, 0)
        } else {
          throw new Error()
        }
      })
    ).subscribe((res) => {
      console.log(res)
      this.rowData = Object.keys(res['armament']).flatMap((key: string) => {
        return res['armament'][key].map((item: string) => ({ item }));
      });
      this.loading = false
    })

  }
}
