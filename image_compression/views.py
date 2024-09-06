from django.shortcuts import render,redirect
from .forms import CompressImageForm
from PIL import Image
import io
# Create your views here.

def compress(request):
    user = request.user
    if request.method == 'POST':
        form = CompressImageForm(request.POST,request.FILES)
        if form.is_valid():
            original_img = form.cleaned_data['original_img']
            quality = form.cleaned_data['quality']
            
            compressed_image = form.save(commit=False)
            compressed_image.user = user
            # perform compression
            img = Image.open(original_img)
            
            output_formate = img.format
            buffer = io.BytesIO()
            img.save(buffer,format=output_formate,quality=quality)
            buffer.seek(0)
            # save the compressed image inside the model
            
            compressed_image.compressed_img.save(
                f'compressed_{original_img}',buffer
            )
            return redirect('compress')
        else:
            # Render the form again with errors if it's invalid
            context = {
                'form': form
            }
            return render(request, 'image_compression/compress.html', context)
    else:
        form = CompressImageForm()
        context = {
            'form':form
        }
        return render(request,'image_compression/compress.html',context)