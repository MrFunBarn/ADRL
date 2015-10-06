from astropy.io import fits

def get_image_type(image,key):
   image = fits.open(image)
   imtype = image[0].header[key]
   return imtype
