from django.shortcuts import render, redirect, HttpResponse
from .models import Profile
from django.template import loader
from xhtml2pdf import pisa
import io

# Create your views here.
def index(request):

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        summary = request.POST.get('summary','')
        skills = request.POST.get('skills','')
        education = request.POST.get('education','')
        institution = request.POST.get('institution','')
        previous_work = request.POST.get('prev_work','')
        
        profile = Profile(name=name, email=email, summary=summary, skills=skills, education=education, institution=institution, previous_work=previous_work)
        profile.save()

        return redirect('preview',id=profile.id)
    return render(request, 'cv/fill.html')

def preview(request, id):
    profile = Profile.objects.get(pk=id)
    skills = profile.skills.split(',')
    template = loader.get_template('cv/cv.html')
    template = template.render(context = {'profile': profile, 'skills':skills})
  
   

        
    # Function to convert HTML to PDF
    def html_to_pdf(html_content):
        result = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html_content.encode("UTF-8")), result)
        if not pdf.err:
            return result.getvalue()
        return None

    # Convert rendered HTML content to PDF
    pdf_file = html_to_pdf(template)

    # Serve the PDF file for download
    if pdf_file:
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
        return response
    else:
        return HttpResponse("Error generating PDF", status=500)


    return render(request,'cv/cv.html',context= {'profile': profile, 'skills':skills})
