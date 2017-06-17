from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

import ingestion.tasks

@login_required
@user_passes_test(lambda u:u.is_superuser)
def ingest_data_by_user_view(request):
    """
    This is a form for an admin user to paste a username into a field
    and press a button to have it scraped and ingested.
    """
    context = {}
    if request.method == 'POST':
        user = request.POST.get('input_name')
        if user:

            success = ingestion.tasks.ingest_data_by_user_wrapper(username=user)
            context['scraped_user'] = user
            context['successful_ingest'] = success


    return render(request, 'admin/ingest-by-user.html', context)