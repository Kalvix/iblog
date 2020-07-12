from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from projects.models import Project, ProjectCategory
from projects import models

# Create your views here.

# def project_index(request):
# 	project = Project.objects.all()
# 	context = {'projects':project}
# 	return render(request,'project_index.html',context)
#

def project_categories(request):
	category = ProjectCategory.objects.all()
	context = {'category':category}
	return render(request,'header.html',context)

def project_detail(request,pk):
	project  = Project.objects.get(pk=pk)
	context = {'project':project}
	return render(request,'project_details.html',context)

def product_detail(request,pk):
	project  = Project.objects.get(pk=pk)
	context = {'project':project}
	return render(request,'product_details.html',context)


class ProductListView(ListView):
	template_name = "project_index.html"
	paginate_by = 3

	def get_queryset(self):
		xx = models.Project.objects.all()

        # tag = self.kwargs["title"]
        # self.title = None

		# if tag != "all":
        #     self.tag = get_object_or_404(
        #         models.Project, title=tag
        #     )
		#
        # if self.tag:
        #     products = models.Project.objects.active().filter(
        #         title=self.title
        #     )
        # else:
        #     products = models.Project.objects.active()
		#
        # return products.order_by("title")


		return xx.order_by("title")