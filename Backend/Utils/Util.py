from Dicts.all_items import all_item_dict
from Dicts.item_dict_temp import item_dict_template

pattern = bytes([0xB0, 0xAD, 0x01, 0x00, 0x01, 0xFF, 0xFF, 0xFF])
pattern_dlc = bytes([0xB0, 0xAD, 0x01, 0x00, 0x01])
isDlcFile = False

def isValidFile(file_read):
    if file_read[:4] != b'BND4':
        return False
    return True


def split(list_a, chunk_size):
    return [list_a[i:i + chunk_size] for i in range(0, len(list_a), chunk_size)]


def getIdReversed(id):
    return ''.join([f'{byte:02X}' for byte in id[:4][::-1]])


def decimalToHex(d, padding=2):
    return f'{d:0{padding}X}'


def buffer_equal(buf1, buf2):
    return buf1 == buf2


def subfinder(mylist, pattern):
    for i in range(len(mylist) - len(pattern) + 1):
        if mylist[i:i+len(pattern)] == pattern:
            return i
    return -1


def getInventory(slot):
    global isDlcFile
    index = subfinder(slot, pattern) + len(pattern) + 8
    if index == -1:
        index = subfinder(slot, pattern_dlc) + len(pattern_dlc) + 3
        isDlcFile = True
    index1 = subfinder(slot[index:], bytes([0] * 50)) + index + 6
    return slot[index:index1]


def getNames(file_read):
    names = []
    for offset in range(0x1901d0e, 0x19031ba + 1, 0x24c):
        name_bytes = file_read[offset:offset + 32]
        name = name_bytes.decode('utf-16').rstrip('\x00')
        names.append(name)
    return names


def get_slot_ls(dat):
    slots = [dat[0x00000310:0x0028030f + 1], dat[0x00280320:0x050031f + 1],
             dat[0x500330:0x78032f + 1], dat[0x780340:0xa0033f + 1],
             dat[0xa00350:0xc8034f + 1], dat[0xc80360:0xf0035f + 1],
             dat[0xf00370:0x118036f + 1], dat[0x1180380:0x140037f + 1],
             dat[0x1400390:0x168038f + 1], dat[0x16803a0:0x190039f + 1]]
    return slots


def getOwnedAndNot(file_read, selected_slot):
    try:
        saves_array = bytearray(file_read)
        slots = get_slot_ls(saves_array)
        inventory = list(getInventory(slots[selected_slot]))
        id_list = split(inventory, 8 if isDlcFile else 16)
        id_list = [getIdReversed(raw_id).upper() for raw_id in id_list]

        owned_items = item_dict_template

        for id in id_list:
            if id in all_item_dict['armament']:
                item = all_item_dict['armament'][id]
                owned_items['armament'][item['category']].append(item['name'])
                del all_item_dict['armament'][id]
            elif id in all_item_dict['armor']:
                item = all_item_dict['armor'][id]
                owned_items['armor'][item['category']].append(item['name'])
                del all_item_dict['armor'][id]
            elif id in all_item_dict['ashesOfWar']:
                item = all_item_dict['ashesOfWar'][id]
                owned_items['ashesOfWar'][item['category']].append(item['name'])
                del all_item_dict['ashesOfWar'][id]
            elif id in all_item_dict['magic']:
                item = all_item_dict['magic'][id]
                owned_items['magic'][item['category']].append(item['name'])
                del all_item_dict['magic'][id]
            elif id in all_item_dict['spiritAshes']:
                owned_items['spiritAshes'].append(all_item_dict['spiritAshes'][id]['name'])
                del all_item_dict['spiritAshes'][id]
            elif id in all_item_dict['talisman']:
                owned_items['talisman'].append(all_item_dict['talisman'][id]['name'])
                del all_item_dict['talisman'][id]

        return owned_items

    except Exception as e:
        return ''
