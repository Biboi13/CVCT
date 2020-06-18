from django.db import models

# Create your models here.

#table_1
class VCT(models.Model):
	vct_name = models.CharField(max_length=200)
	vct_active_users = models.CharField(max_length=200)
	vct_developer = models.CharField(max_length=200)
	
	def __str__(self):
		return self.vct_name
#table_2
class Prob_occur(models.Model):
	probl_occur_name = models.CharField(max_length=200)

	def __str__(self):
		return self.probl_occur_name
#table_3
class Individual(models.Model):
    indv_name       = models.CharField(max_length=200)
    indv_place      = models.CharField(max_length=200)
    indv_used_vct   = models.ForeignKey(VCT, on_delete=models.CASCADE)
    indv_internet_bandwidth = models.CharField(max_length=200)
    indv_problem_occurred   = models.ForeignKey(Prob_occur, on_delete=models.CASCADE)
    indv_satifactory        = models.CharField(max_length=200)
    indv_started_using_vct_name = models.DateField('date published')
    indv_recommend_vct          = models.CharField(max_length=200)
    
    def __str__(self):
	    return self.indv_name
#table_4
class Organization(models.Model):
    org_name       = models.CharField(max_length=200)
    org_place      = models.CharField(max_length=200)
    org_used_vct   = models.ForeignKey(VCT, on_delete=models.CASCADE)
    org_internet_bandwidth = models.CharField(max_length=200)
    org_problem_occurred   = models.ForeignKey(Prob_occur, on_delete=models.CASCADE)
    org_satifactory        = models.CharField(max_length=200)
    org_started_using_vct_name = models.DateField('date published')
    org_recommend_vct          = models.CharField(max_length=200)
    
    def __str__(self):
	    return self.org_name

