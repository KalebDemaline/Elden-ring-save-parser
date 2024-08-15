import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ParseService {

  constructor(private http: HttpClient) { }

  private url = 'http://localhost:9999'

  getCharacterInfo(user_id: string, character_index: number): Observable<any>{
    return this.http.get(`${this.url}/read?user_id=${user_id}&character_index=${character_index}`)
  }

  getCharacterNames(user_id: string, character_index: number): Observable<string[]>{
    return this.http.get<string[]>(`${this.url}/names?user_id=${user_id}&character_index=${character_index}`)
  }

  sendSaveFile(user_id: string, save_file: File): Observable<number>{
    const formData = new FormData();
    formData.append('user_id', user_id);
    formData.append('save_file', save_file);

    return this.http.post<number>(`${this.url}`, formData);
  }
}