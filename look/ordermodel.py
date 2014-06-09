class Order(models.Model):
    date_asked
    date_due
    owner
    writer
    pages
    words
    type(list)
    topic
    discpline
    service (writing from scrtch, rewriting, editing)
    citation (mla, apa, chicago/tarubian, other )
    further_instructions
    additional materials
    prefered writer
    bids
    bid_prices M2M
    isPaidfor
    progress
    
    