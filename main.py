import qrcode
feat=qrcode.QRCode(version=1,box_size=40, border=4)
feat.add_data('https://www.youtube.com/c/durgasoftvideos')
feat.make(fit=True)
generate_img=feat.make_image(fill_color='blue', back_color='white')

generate_img.save('image2.png')





# generator_img=qrcode.make('Chandan Nepali hai.... aur ajit farzi hai...')
# generator_img.save('image1.png')
