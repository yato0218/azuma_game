# coding: UTF-8
import qrcode  # ライブラリのインポート
img = qrcode.make('https://yato0218.github.io/azuma_game/')  # QRコードの作成(括弧内にアクセスしたいurlを書く)
img.show()  # QRコードを表示
img.save('QR_01_plus_N_game.png')  # 生成するQRコードの名称を指定して保存
