from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.core.files.storage import FileSystemStorage
from .forms import SignUpForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import ContactForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def post_detail(request, slug):

        template_name = 'post_detail.html'
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        new_comment = None
        # Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        else:
            comment_form = CommentForm()

        return render(request, template_name, {'post': post,
                                            'comments': comments,
                                           'new_comment': new_comment,'comment_form': comment_form})
def currency(request):
      template = 'currency.html'
      return render(request, template)

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
 
            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

# def base(request):
#       template1 = 'base.html'
#       return render(request, template1)


# def post_detail(request):
#       template2 = 'post_detail.html'
#       return render(request, template2)

# def sidebar(request):
#       template3 = 'sidebar.html'
#       return render(request, template3)