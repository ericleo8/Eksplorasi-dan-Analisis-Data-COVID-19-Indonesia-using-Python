import requests
resp = requests.get(
    'https://storage.googleapis.com/dqlab-dataset/update.json', verify=False)
print(resp)
print(resp.headers)
cov_id_raw = resp.json()

print('Length of cov_id_raw : %d.' % len(cov_id_raw))
print('Komponen cov_id_raw  : %s.' % cov_id_raw.keys())
cov_id_update = cov_id_raw['update']

print('Tanggal pembaharuan data penambahan kasus   :',
      cov_id_update['penambahan']['tanggal'])
print('Jumlah penambahan kasus sembuh :',
      cov_id_update['penambahan']['jumlah_sembuh'])
print('Jumlah penambahan kasus meninggal :',
      cov_id_update['penambahan']['jumlah_meninggal'])
print('Jumlah total kasus positif hingga saat ini :',
      cov_id_update['total']['jumlah_positif'])
print('Jumlah total kasus meninggal hingga saat ini :',
      cov_id_update['total']['jumlah_meninggal'])

resp_jabar = requests.get(
    'https://storage.googleapis.com/dqlab-dataset/prov_detail_JAWA_BARAT.json', verify=False)
cov_jabar_raw = resp_jabar.json()

resp_jabar = requests.get(
    'https://storage.googleapis.com/dqlab-dataset/prov_detail_JAWA_BARAT.json', verify=False)
cov_jabar_raw = resp_jabar.json()

print('Nama-nama elemen utama:\n', cov_jabar_raw.keys())
print('\nJumlah total kasus COVID-19 di Jawa Barat                 : %d' %
      cov_jabar_raw['kasus_total'])
print('Persentase kematian akibat COVID-19 di Jawa Barat         : %f.2%%' %
      cov_jabar_raw['meninggal_persen'])
print('Persentase tingkat kesembuhan dari COVID-19 di Jawa Barat : %f.2%%' %
      cov_jabar_raw['sembuh_persen'])

cov_jabar = pd.DataFrame(cov_jabar_raw['list_perkembangan'])
print('Info cov_jabar:\n', cov_jabar.info())
print('\nLima data teratas cov_jabar:\n', cov_jabar.head())
