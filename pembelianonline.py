data_product = {
    1:"Laptop",
    2:"Mouse",
    3:"Monitor",
    4:"MousePad",
    5:"Charger",
}
daftar_harga = {
    1: 2000000,
    2: 50000,
    3: 600000,
    4: 30000,
    5: 15000,
}

dict_trx = {}
daftar_metode_pembayaran  = {
    1: "Transfer Bank",
    2: "Virtual Account",
    3: "Cash On Delivery",
    4: "Kartu Kredit",
}
print("========== List Product ==========")
for i in data_product:
    print("Id Product : ",i, "\t Nama Product : ",data_product[i],"\t Harga Product : ",daftar_harga[i])

pilih_id = int(input("Pilih Id Product : "))
if pilih_id in data_product :
    pilih_beli = input("Ingin Beli ?? (Y/N): ")
    if pilih_beli == "y" or pilih_beli == "Y":
        nama_penerima = input("Nama Penerima : ")
        alamat_penerima = input("Alamat Penerima : ")
        telepon = input("Nomor HP Penerima : ")
        kurir_pengiriman = input("Kurir Pengiriman : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "no hp":telepon,
            "kurir pengiriman":kurir_pengiriman,
            "product id":data_product,
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("==================== Metode Pembayaran ====================")
    for i in daftar_metode_pembayaran:
        print("Id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih ID MEtode Pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : ", dict_trx["nama penerima"]),
        print("Alamat Penerima : ", dict_trx["alamat penerima"]),
        print("Nomor Hp : ", dict_trx["no hp"]),
        print("Kurir Pengiriman : ", dict_trx["kurir pengiriman"]),
        print("Product : ", data_product[pilih_id]),
        print("Harga : ", daftar_harga[pilih_id]),
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode]),
        konfirmasi = input("Apakah Yakin? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("Anda Sudah Berhasil Melakukan Pembayaran")
        else:
            pass
    else:
        print("Metode Pembayaran Tidak Tersedia!!!")
else:
    print("Id Product Tidak Tersedia!!!")