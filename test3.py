import streamlit as st
import pandas as pd

# Menampilkan slide untuk pendahuluan
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px;'>
        <h2 style='color: #333333; text-align:center;'>Selamat Datang di Aplikasi Menghitung Kalori Buah</h2>
        <p style='color: #333333; text-align:justify;'>Aplikasi ini dirancang untuk membantu Anda menghitung jumlah kalori dalam berbagai jenis buah. 
        Pilih buah favorit Anda, masukkan beratnya, dan aplikasi kami akan memberikan informasi tentang jumlah kalori serta kandungan nutrisinya. 
        Selain itu, Anda juga dapat menemukan rekomendasi buah berdasarkan jumlah kalori yang Anda inginkan.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Informasi tambahan tentang manfaat kesehatan, cara memilih buah yang baik, dan resep
informasi_tambahan = {
    'apel': {
        'manfaat': "Apel mengandung serat yang baik untuk pencernaan dan antioksidan yang dapat membantu menjaga kesehatan jantung.",
        'cara_memilih': "Pilih apel yang berwarna cerah, beratnya padat, dan tanpa memar. Hindari apel yang terlalu lembek.",
        'resep': "Resep sehat: Salad apel dengan kacang almond dan saus yogurt."
    },
    'pisang': {
        'manfaat': "Pisang kaya akan kalium yang baik untuk kesehatan jantung dan membantu menjaga tekanan darah.",
        'cara_memilih': "Pilih pisang yang kulitnya tidak terlalu berwarna hijau dan tidak terlalu berwarna cokelat. Pilih yang masih dalam kondisi sedikit kehijauan.",
        'resep': "Resep sehat: Smoothie pisang dengan bayam dan susu almond."
    },
    'jeruk': {
        'manfaat': "Jeruk kaya akan vitamin C yang baik untuk sistem kekebalan tubuh dan mengandung antioksidan untuk kesehatan kulit.",
        'cara_memilih': "Pilih jeruk yang beratnya padat dan berwarna cerah. Hindari jeruk yang terlalu lembek atau memiliki bintik-bintik coklat.",
        'resep': "Resep sehat: Jus jeruk segar tanpa gula tambahan."
    },
    'pir': {
        'manfaat': "Pir mengandung serat yang baik untuk pencernaan dan mengandung antioksidan yang membantu menjaga kesehatan tubuh.",
        'cara_memilih': "Pilih pir yang berwarna cerah dan padat. Hindari pir yang terlalu lembek atau memiliki bintik-bintik coklat.",
        'resep': "Resep sehat: Salad pir dengan keju feta dan dressing lemon."
    },
    'strawberry': {
        'manfaat': "Stroberi kaya akan vitamin C dan antioksidan yang baik untuk kesehatan jantung dan kulit.",
        'cara_memilih': "Pilih stroberi yang berwarna cerah, tanpa noda hitam, dan berukuran sedang.",
        'resep': "Resep sehat: Smoothie stroberi dengan yogurt dan madu."
    },
    'semangka': {
        'manfaat': "Semangka mengandung air yang tinggi, membantu menjaga hidrasi tubuh, dan mengandung antioksidan untuk kesehatan kulit.",
        'cara_memilih': "Pilih semangka yang beratnya padat dan memiliki bintik kuning di bagian bawahnya.",
        'resep': "Resep sehat: Salad semangka dengan mentimun dan keju feta."
    },
    'mangga': {
        'manfaat': "Mangga mengandung vitamin A dan C yang baik untuk kesehatan mata dan sistem kekebalan tubuh.",
        'cara_memilih': "Pilih mangga yang berwarna cerah, beratnya padat, dan sedikit memberi aroma di pangkalnya.",
        'resep': "Resep sehat: Smoothie mangga dengan pisang dan yogurt."
    },
    'alpukat': {
        'manfaat': "Alpukat kaya akan lemak sehat, serat, dan vitamin K. Baik untuk kesehatan jantung dan otak.",
        'cara_memilih': "Pilih alpukat yang memberi sedikit tekanan ketika ditekan dan beratnya terasa padat.",
        'resep': "Resep sehat: Guacamole dengan alpukat, tomat, bawang merah, dan perasan lemon."
    },
    'kurma': {
        'manfaat': "Kurma merupakan sumber energi yang baik dan mengandung banyak mineral seperti potassium, magnesium, dan zat besi.",
        'cara_memilih': "Pilih kurma yang berwarna cerah dan lembut, hindari yang terlalu kering.",
        'resep': "Resep sehat: Energy balls dengan kurma, almond, dan biji chia."
    },
    'anggur': {
        'manfaat': "Anggur mengandung antioksidan dan memiliki manfaat bagi kesehatan jantung dan fungsi otak.",
        'cara_memilih': "Pilih anggur yang berwarna cerah, padat, dan tanpa keriput. Hindari yang terlalu lembek atau berlendir.",
        'resep': "Resep sehat: Salad anggur dengan keju gorgonzola dan kacang kenari."
    },
    'nanas': {
        'manfaat': "Nanas mengandung enzim bromelain yang baik untuk pencernaan dan mengandung vitamin C yang tinggi.",
        'cara_memilih': "Pilih nanas yang berwarna cerah dan berbau harum di bagian bawahnya.",
        'resep': "Resep sehat: Smoothie nanas dengan kelapa dan mint."
    },
    'kiwi': {
        'manfaat': "Kiwi kaya akan vitamin C dan serat yang baik untuk pencernaan.",
        'cara_memilih': "Pilih kiwi yang memberi sedikit tekanan ketika ditekan, hindari yang terlalu lembek.",
        'resep': "Resep sehat: Salad kiwi dengan stroberi dan daun selada."
    },
    'apel hijau': {
        'manfaat': "Apel hijau kaya akan serat dan vitamin C. Baik untuk pencernaan dan menjaga sistem kekebalan tubuh.",
        'cara_memilih': "Pilih apel hijau yang berwarna cerah dan beratnya padat.",
        'resep': "Resep sehat: Smoothie apel hijau dengan bayam dan madu."
    },
  }

# Tambahkan tautan ke informasi tambahan untuk buah yang dipilih
st.sidebar.title('Informasi Tambahan')
buah_info = st.sidebar.selectbox('Pilih Buah', list(informasi_tambahan.keys()), format_func=lambda x: x.capitalize())

# Tambahkan fitur interaktif untuk membuka atau menutup informasi tambahan
if buah_info:
    if st.sidebar.checkbox('Tampilkan Informasi Tambahan'):
        st.sidebar.subheader('Manfaat Kesehatan:')
        st.sidebar.write(informasi_tambahan[buah_info]['manfaat'])

        st.sidebar.subheader('Cara Memilih Buah yang Baik:')
        st.sidebar.write(informasi_tambahan[buah_info]['cara_memilih'])

        st.sidebar.subheader('Resep:')
        st.sidebar.write(informasi_tambahan[buah_info]['resep'])

# Melanjutkan dengan kode aplikasi Streamlit Anda seperti biasa


kalori_buah = {
    'apel': {
        'kalori': 52,
        'vitamin': {'Vitamin A': '3%', 'Vitamin C': '14%'},
        'serat': '2.4g',
        'protein': '0.3g',
        'lemak': '0.2g'
    },
    'pisang': {
        'kalori': 89,
        'vitamin': {'Vitamin B6': '20%', 'Vitamin C': '14%'},
        'serat': '2.6g',
        'protein': '1.1g',
        'lemak': '0,3g'
    },
    'jeruk': {
        'kalori': 43,
        'vitamin': {'Vitamin C': '90%'},
        'serat': '2.4g',
        'protein': '0.9g',
        'lemak': '0.2g'
    },
    'pir': {
        'kalori': 57,
        'vitamin': {'Vitamin C': '7%'},
        'serat': '2.4g',
        'protein': '0.4g',
        'lemak': '0.2g'
    },
    'strawberry': {
        'kalori': 32,
        'vitamin': {'Vitamin C': '98%'},
        'serat': '2g',
        'protein': '0.7g',
        'lemak': '0.3g'
    },
    'semangka': {
        'kalori': 30,
        'vitamin': {'Vitamin A': '11%', 'Vitamin C': '13%'},
        'serat': '0.4g',
        'protein': '0.6g',
        'lemak': '0.2g'
    },
    'mangga': {
        'kalori': 60,
        'vitamin': {'Vitamin A': '25%', 'Vitamin C': '76%'},
        'serat': '1.6g',
        'protein': '0.8g',
        'lemak': '0.4g'
    },
    'alpukat': {
        'kalori': 160,
        'vitamin': {'Vitamin K': '26%', 'Vitamin E': '14%'},
        'serat': '6.7g',
        'protein': '2g',
        'lemak': '14.7g'
    },
    'kurma': {
        'kalori': 282,
        'vitamin': {'Vitamin B6': '10%', 'Vitamin C': '3%'},
        'serat': '8g',
        'protein': '2.2g',
        'lemak': '0.2g'
    },
    'anggur': {
        'kalori': 67,
        'vitamin': {'Vitamin C': '5%', 'Vitamin K': '18%'},
        'serat': '0.9g',
        'protein': '0.6g',
        'lemak': '0.2g'
    },
    'nanas': {
        'kalori': 50,
        'vitamin': {'Vitamin C': '79%'},
        'serat': '1.4g',
        'protein': '0.5g',
        'lemak': '0.1g'
    },
    'kiwi': {
        'kalori': 61,
        'vitamin': {'Vitamin C': '112%', 'Vitamin K': '38%'},
        'serat': '2.1g',
        'protein': '1.1g',
        'lemak': '0.5g'
    },
    'rambutan': {
        'kalori': 68,
        'vitamin': {'Vitamin C': '44%'},
        'serat': '0.9g',
        'protein': '0.9g',
        'lemak': '0.2g'
    },
    'pepaya': {
        'kalori': 43,
        'vitamin': {'Vitamin C': '148%', 'Vitamin A': '31%'},
        'serat': '1.7g',
        'protein': '0.5g',
        'lemak': '0.3g'
    },
    'lemon': {
        'kalori': 29,
        'vitamin': {'Vitamin C': '64%'},
        'serat': '2.8g',
        'protein': '1.1g',
        'lemak': '0.3g'
    },
    'markisa': {
        'kalori': 97,
        'vitamin': {'Vitamin C': '20%'},
        'serat': '2.4g',
        'protein': '2.2g',
        'lemak': '0.7g'
    },
    'kelapa': {
        'kalori': 354,
        'vitamin': {'Vitamin C': '3%', 'Vitamin B6': '5%'},
        'serat': '9g',
        'protein': '3.3g',
        'lemak': '33.5g'
    },
    'durian': {
        'kalori': 150,
        'vitamin': {'Vitamin C': '47%', 'Vitamin B6': '10%'},
        'serat': '3.8g',
        'protein': '1.5g',
        'lemak': '5.3g'
    },
    'salak': {
        'kalori': 82,
        'vitamin': {'Vitamin C': '8%'},
        'serat': '2.6g',
        'protein': '0.6g',
        'lemak': '0.7g'
    },
    'melon': {
        'kalori': 34,
        'vitamin': {'Vitamin A': '12%', 'Vitamin C': '61%'},
        'serat': '0.6g',
        'protein': '0.9g',
        'lemak': '0.2g'
    },
    'blueberry': {
        'kalori': 57,
        'vitamin': {'Vitamin C': '16%', 'Vitamin K': '24%'},
        'serat': '2.4g',
        'protein': '0.7g',
        'lemak': '0.3g'
    },
    'delima': {
        'kalori': 83,
        'vitamin': {'Vitamin C': '17%', 'Vitamin K': '16%'},
        'serat': '4g',
        'protein': '1.7g',
        'lemak': '1.2g'
    },
    
    'buah naga': {
        'kalori': 60,
        'vitamin': {'Vitamin C': '9%', 'Vitamin B3': '8%'},
        'serat': '3g',
        'protein': '1.2g',
        'lemak': '0.6g'
    },
    'cherry': {
        'kalori': 50,
        'vitamin': {'Vitamin C': '12%', 'Vitamin K': '9%'},
        'serat': '2.5g',
        'protein': '1g',
        'lemak': '0.3g'
    },
    'kiwi': {
        'kalori': 61,
        'vitamin': {'Vitamin C': '112%', 'Vitamin K': '38%'},
        'serat': '2.1g',
        'protein': '1.1g',
        'lemak': '0.5g'
    },
    'kelengkeng': {
        'kalori': 64,
        'vitamin': {'Vitamin C': '90%', 'Vitamin B6': '5%'},
        'serat': '1.3g',
        'protein': '0.9g',
        'lemak': '0.5g'
    },
    'belimbing': {
        'kalori': 31,
        'vitamin': {'Vitamin C': '52%', 'Vitamin A': '2%'},
        'serat': '1.6g',
        'protein': '1.2g',
        'lemak': '0.2g'
    },
    'manggis': {
        'kalori': 73,
        'vitamin': {'Vitamin C': '33%', 'Vitamin B6': '5%'},
        'serat': '0.5g',
        'protein': '0.5g',
        'lemak': '0.2g'
    },
    'sawo': {
        'kalori': 137,
        'vitamin': {'Vitamin C': '24%', 'Vitamin A': '5%'},
        'serat': '5.3g',
        'protein': '0.8g',
        'lemak': '0.6g'
    },
    'langsat': {
        'kalori': 60,
        'vitamin': {'Vitamin C': '33%', 'Vitamin B6': '5%'},
        'serat': '2.3g',
        'protein': '0.9g',
        'lemak': '0.2g'
    },
    'duku': {
        'kalori': 81,
        'vitamin': {'Vitamin C': '31%', 'Vitamin A': '3%'},
        'serat': '1.8g',
        'protein': '0.7g',
        'lemak': '0.3g'
    },
    'kismis': {
        'kalori': 299,
        'vitamin': {'Vitamin C': '1%', 'Vitamin K': '1%'},
        'serat': '3.7g',
        'protein': '3.1g',
        'lemak': '0.5g'
    },
    'nangka': {
        'kalori': 95,
        'vitamin': {'Vitamin C': '23%', 'Vitamin A': '2%'},
        'serat': '2.6g',
        'protein': '1.7g',
        'lemak': '0.3g'
    },
    'sirsak': {
        'kalori': 66,
        'vitamin': {'Vitamin C': '24%', 'Vitamin B6': '5%'},
        'serat': '3.3g',
        'protein': '1g',
        'lemak': '0.3g'
    },
    'srikaya': {
        'kalori': 148,
        'vitamin': {'Vitamin C': '20%', 'Vitamin A': '2%'},
        'serat': '3.3g',
        'protein': '1.6g',
        'lemak': '0.9g'


    }
}

# Sekarang lanjutkan dengan kode aplikasi Streamlit Anda seperti biasa

st.title('Menghitung Kalori Buah')
st.write("Selamat datang di aplikasi menghitung kalori buah. Pilih buah favorit Anda dan berapa beratnya, lalu kami akan memberi tahu Anda jumlah kalori yang terkandung.")
buah = st.selectbox('Pilih Buah', list(kalori_buah.keys()), format_func=lambda x: x.capitalize())

berat = st.slider('Berat (gram)', min_value=1, max_value=5000, value=100)

if st.button('Hitung Kalori'):
    kalori_total = (kalori_buah[buah]['kalori'] / 100) * berat
    st.write(f"Jumlah kalori dalam {berat} gram {buah} adalah: {kalori_total} kalori")
    st.write("Informasi Nutrisi:")
    st.write(f"- Serat: {kalori_buah[buah]['serat']}")
    st.write(f"- Protein: {kalori_buah[buah]['protein']}")
    st.write(f"- Lemak: {kalori_buah[buah]['lemak']}")
    st.write("Kandungan Vitamin:")
    for vitamin, nilai in kalori_buah[buah]['vitamin'].items():
        st.write(f"- {vitamin}: {nilai}")
    

# Tambahkan rekomendasi buah berdasarkan jumlah kalori yang dipilih
st.sidebar.title('Rekomendasi Buah Berdasarkan Kalori')
kalori_target = st.sidebar.slider('Pilih Jumlah Kalori', min_value=10, max_value=1000, value=100)
st.sidebar.write('Buah-buahan dengan kalori serupa:')
for buah, info in kalori_buah.items():
    if abs((info['kalori'] / 100) * berat - kalori_target) < 20:
        st.sidebar.write(f"- {buah.capitalize()}")



