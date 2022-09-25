from django.db import models

# class AddressField(models.Field):
#     def __init__(self, *args, **kwargs):
#         self.country = kwargs.pop('max_upload_size', [])
#         self.state = 
#         self.street_adress =
#         self.zipcode =
#         super().__init__(*args, **kwargs)
    

    ### IMPLEMENT IF THERE IS ANYTHING THAT IS INVALID LIKE WRONG ADRESS
    # def clean(self, *args, **kwargs):
    #     data = super(FileField,self).clean(*args, **kwargs)
    #     file = data.file
    #     try:
    #         if file.size > self.max_upload_size:
    #             raise forms.ValidationError('Please keep filesize under {}. Current filesize {}'.format(filesizeformat(self.max_upload_size), filesizeformat(file.size)),code="invalid")
    #     except AttributeError:
    #         pass
    #     return data