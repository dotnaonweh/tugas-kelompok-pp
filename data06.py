def baca_data06():
    file = open("data06.txt", "r")
    for i in file:
        tim1, skor1, skor2, tim2 = i.split()
        dict_kosong.append({
            "Team 1": tim1,
            "Gol Dicetak Team 1": int(skor1),
            "Gol Dicetak Team 2": int(skor2),
            "Team 2": tim2,
        })
    file.close()
    return dict_kosong

dict_kosong = []
def cari_pemenang(dict_kosong):
    if dict_kosong['Gol Dicetak Team 1'] > dict_kosong['Gol Dicetak Team 2']:
        dict_kosong['Hasil'] = 'Team'+ ' ' +dict_kosong['Team 1']+ ' ' +'Menang'
    elif dict_kosong['Gol Dicetak Team 1'] < dict_kosong['Gol Dicetak Team 2']:
        dict_kosong['Hasil'] = 'Team '+ ' ' +dict_kosong['Team 2']+ ' ' +'Menang'
    else:
        dict_kosong['Hasil'] = 'Pertandingan Seri'


    return dict_kosong
def main():
    baca_data06()
    nilai_siswa = list(map(cari_pemenang, dict_kosong))
    print(nilai_siswa)
main()