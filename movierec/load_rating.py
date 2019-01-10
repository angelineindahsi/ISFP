import sys, os
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movierec.settings")

import django
django.setup()

from recsite.models import Review
from recsite.models import Movie
from django.contrib.auth.models import User


def save_review_from_row(review_row):
    review = Review()
    review.user_id = User.objects.get(id=review_row[0])
    review.user_name = User.objects.get(id=review_row[0])
    review.movie = Movie.objects.get(id=review_row[1])
    review.rating = review_row[2]
    review.pub_date = datetime.datetime.now()
    review.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print ("Reading from file ",str(sys.argv[1]))
        ratingdf = pd.read_csv(sys.argv[1],error_bad_lines=False)
        print (ratingdf)

        ratingdf.apply(
            save_review_from_row,
            axis=1
        )

        print ("There are {} reviews ".format(Review.objects.count()))
        
    else:
        print ("Please, provide rating file path")
