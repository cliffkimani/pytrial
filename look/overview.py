pages:

#Home
    #Our rates
    #Already There Links
    

#functional pages (generic)

User: (admin, customers, writer)
    Login
    Logout
    
    
    if user is admin => admin landing page
    elif user is writer => writer landing page
    else user has to be customer => customer landing page
    
#Writer:
    Writer landing page => use jimmy type 
        Available jobs
        My Bids
        Completed Jobs
        Jobs Under review
        Jobs Due
        Current Revisions
            Revision rate
        My messages
            Inbox
            Sent
            
        Writers Guide
            Writers pannel
            Paper Formatting
            Plagiarism
            Referencing Styles
                MLA
                APA
                Chicago and Tarubian
                Havard
                Griffith Referencing Tool
            Terms and conditions   
    Account
        Private Profile
            Change Password
            Change Details
            Payment Method
        Public Profile
            As seen by clients
    
    Reports
        My Payments
        View Weekly Reports
        View Monthly Reports
    
    Top Earners:
        Table Format    
    
    Jobs status => has to be editable and usable
    Payment => request payment plus ideal bal and ripe balance
    writers rules and regulations
    writer FAQ
    
    
    register:
        names (2)
        nick name (1)
        headshot (image)
        writer ID: six digit number
        date of birth
        academic qualifications
        
    


#Customer:
    Customer Landing page after log in
    Customer Quick registration page
    Make a new order => @Registered
       1.   Email
            Type of Paper
            Pages
            Deadline (Date and Time)
            
                what next, days left widget
       2.   On continue:
                automatic registration
                automatic log in
                automated password sent to email
       3.   Customer view page (See screen shots)          
            + Orders
            + My profile
            + Balance
            + Refer a friend
            + Support
            + New Order
            + Fill in Order details
            + Pay for the order to engage a writer
            + Work Progress
                + Approve the order marked as complete
                + Send a revision
                + Send a tip
                + Rate writer
                + Download Final document
                
#admin:
    Admin landing page
    Admin backend? to add users
    
    #Order management
    New orders
    Un allocated orders
        +Allow express bidding
    Change base order prices
        (Field, Base, Urgency)
    
    
    #Writer management
    Approve New Writers(N)
    Pay Writers (N)
    
    
    
    #Customer management
    Support inquiries(N)
    Cancel an order
    Refund order money



#job management:
    Job landing page: @login_required
    
    if Admin:
        show this:
    elif writer:
        show this: (owner only unless not allocated)
    else:
        show this for clients (owner only)
    
    Homepage
        (has user, bids, customer, 
    
    
    
#On Base
    Template 
    If user.is_authenticated => combo with options Logout, My profile, My orders, Balance, Support, New order
    
    else guest login


