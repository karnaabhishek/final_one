import qrcode
img = qrcode.make('otpauth://totp/admin?secret=PMFSYCR67HWHB3HAJSS7HEZ2PHGSZG6A&algorithm=SHA1&digits=6&period=30')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")