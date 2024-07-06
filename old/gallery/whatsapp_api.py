from whatsapp import WhatsApp

def send_whatsapp_message(phone_number, message):
    whatsapp = WhatsApp(token="your_whatsapp_api_token")
    response = whatsapp.send_message(phone_number, message)
    return response

# Add this function to your views.py
def contact_admin_whatsapp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        response = send_whatsapp_message(phone_number, message)
        # Handle the response and return appropriate feedback to the user
    return render(request, 'gallery/contact_admin_whatsapp.html')