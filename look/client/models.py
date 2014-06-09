from django.db import models

class Client(models.Model):
    fname
    lname
    email
    timezone
    orders
    balance
    queries
    refferals
    offer notofications?
    service news notfication?
    nickname
    headshot
    
    id
    sw_id
    dob
    qualifications (grad, postgrad, etc)
    major
    gradyear
    paid_jobs
    rejected_jobs
    total_spent
    balance
    is_active
    
    current_jobs = models.IntegerField()
    pending_jobs
    due_jobs
    revisions
    inbox
    sent
    total_tipped
    tips_number
    rating
    