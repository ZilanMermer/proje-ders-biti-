import discord
from discord.ext import commands
import os

# Botun Discord API'ye bağlanması için gerekli izinler
intents = discord.Intents.default()
intents.message_content = True  # Botun mesaj içeriğine erişimine izin veriyoruz.

# Botu başlatıyoruz
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık!')  # Botun başarılı bir şekilde bağlandığını belirten mesaj

# iklim hakkında tavsiyeler veren komut
@bot.command()
async def iklim_tavsiyesi(ctx):
    tavsiyeler = [
       "Fosil yakıt kullanımı yerine yenilenebilir enerji kaynaklarını tercih edin.",
        "Araba yerine yürüyüş veya bisiklet kullanarak karbon ayak izinizi azaltın.",
        "Enerji tasarruflu ampuller kullanarak elektrik tüketimini düşürün.",
        "Evde ısı yalıtımı yaparak enerji kaybını önleyin.",
        "Geri dönüşümlü ve sürdürülebilir ürünler tercih edin.",
        "Et tüketimini azaltarak metan gazı salınımını düşürün.",
        "Su tasarrufu yaparak enerji tüketimini ve sera gazlarını azaltın.",
        "Toplu taşıma ve paylaşımlı araç kullanımıyla karbon salımını azaltın."
    ]
    await ctx.send("🌍 Bugünün iklim dostu tavsiyeleri:\n" + "\n".join(f"- {t}" for t in tavsiyeler)) # Kullanıcıya tavsiyeleri sıralı şekilde gönderir
    with open('images/iklim tavsiyesi.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
        # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    #iklim değişikliğiyle  ilgili link komutu
    await ctx.send( "İklim tavsiyesi  görseli: https://www.enuygun.com/bilgi/gezegenimiz-icin-en-buyuk-tehdit-iklim-krizi/ ")




#Karbon ayak izi hakkında bilgi veren komut
@bot.command()
async def karbon_ayak_izi(ctx):
    await ctx.send(
        " Karbon Ayak İzi, bireylerin veya kuruluşların günlük faaliyetleri sonucu atmosfere saldıkları "
        "sera gazı miktarını ifade eder. Azaltmak için enerji tasarrufu, toplu taşıma ve sürdürülebilir ürünler kullanabilirsiniz."
    )
    with open('images/karbon ayak izi.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    #karbon ayak izi hakkında bilgi verdkten sonra karbon ayak iziyle ilgili link vericek komut
    await ctx.send( "Karbon ayak izi  görseli: https://turkkep.com.tr/karbon-ayak-izi-hakkinda-bilmeniz-gerekenler/ ")
  


#Sera etkisi hakkında bilgi veren komut
@bot.command()
async def sera_etkisi(ctx):
    await ctx.send(
        " Sera etkisi, atmosferde biriken gazların (CO₂, CH₄, N₂O gibi) Dünya'nın sıcaklığını artırmasıdır. "
        "Bu, küresel ısınmaya ve iklim değişikliğine yol açar."
    )
    with open('images/sera etkisi.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    #sera etkisi hakkında bilgi verdikten sonra sera etkisi ile ilgili link vericek komut
    await ctx.send( "Sera etkisi görseli: https://bilimgenc.tubitak.gov.tr/makale/iklim-degisikliginin-sebepleri-nelerdir")





#İklim değişikliğiyle mücadele önerileri veren komut
@bot.command()
async def iklim_mucadele(ctx):
    # Kullanıcıya iklim değişikliğiyle mücadelede neler yapabileceğini sıralar
    await ctx.send(
        "⚡ İklim Değişikliğiyle Mücadele İçin:\n"
        "1️⃣ Yenilenebilir enerji kullanın.\n"
        "2️⃣ Enerji tasarrufu yapın.\n"
        "3️⃣ Geri dönüşüme önem verin.\n"
        "4️⃣ Karbon ayak izinizi azaltmaya çalışın.\n"
        "5️⃣ Doğa dostu ulaşım yöntemlerini tercih edin."
    )


#Botun çalışmasını sağlayan ana kod, token ile Discord'a bağlanır
bot.run()
