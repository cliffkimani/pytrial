from django.db import models

class Writer(models.Model):
    fname
    lname
    nickname
    headshot
    email
    timezone
    rating
    id
    sw_id
    dob
    qualifications (grad, postgrad, etc)
    major
    gradyear
    paid_earnings
    balance
    ripe_balance
    payment_mode (paypal, mpesa, bank etc)
    is_hired
    is_active
    
    
    
    available_jobs = models.IntegerField()
    bids
    completed_jobs
    pending_jobs
    due_jobs
    revisions
    inbox
    sent
    