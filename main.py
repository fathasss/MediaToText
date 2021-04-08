# %%
# Kütüphanenin import edilmesi
import speech_recognition as ses_tanima

#recognizer sınıfının tanıtılması
sesi_tani = ses_tanima.Recognizer()

# %%
#Kayıdın okutulması
with ses_tanima.AudioFile('kayit.wav') as kaynak:

    ses_metni = sesi_tani.listen(kaynak)

    try:
        # Google ses tanıma servisini kullan
        text = sesi_tani.recognize_google(ses_metni, language = "tr-TR")
        print('Ses Dönüşümü:')
        print(text)
        
    except:
         print('ERROR 404')
# %%
