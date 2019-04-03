Model Architecture Planning

# 5 core models :
Membership -  make in the beginning and never touch again- a reference object
    - slug
    - type (free, pro, enterrprise)
    - price 
    - stripe plan id (billing in stripe needs differecnt plans)
    
UserMembership - references type of memebership created initally
    - user  (foreign key to default user)
    - stripe customer id ( stripe backend requires this)
    - membership type (foreign key to membership)

Subscription - only created when a member creates a a paid membership
    - user membership (foreign key to UserMembership)
    - stripe subscription id  (created when a user pays)
    - active 

Course
    - slug
    - title
    - description
    - allowed memberships (foreign key to Membership) - describes which membership can view

Lesson
    - slug
    - title
    - description
    - Course  (foreign ket to Course)
    - position (use int instead of primary key so it is not affected when courses are deleted)
    - video
    - thumbnail
