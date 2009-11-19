#!/usr/bin/python

import digichef

from digichef.recipes.models import *
from digichef.tagging.models import *


from django.contrib.auth.models import User

def load_data():

	print "deleting auth database (or most of it)..."
	users = User.objects.all()
	#Cheers :)
	for user in users:
		user.delete()

	print "Loading basic data into database..."

	#===============PEOPLE======================

	p = User(
	username='rob',
	first_name='Rob',
	last_name='Miles',
	is_superuser=1,
	is_staff=1,
	email="afromonkey0@gmail.com"
	)
	p.save()
	p.set_password("iamrob")
	p.save()

	p = User(
	username='dhruv',
	first_name='Dhruv',
	last_name='Gairola',
	is_superuser=1,
	is_staff=1,
	email="" #idk
	)
	p.save()
	p.set_password("iamdhruv")
	p.save()
	

	#===============RECIPES======================
	
	r = Recipe(
	title='Blueberry Peach Muffins',
	ingredients="""375 g all-purpose flour
100 g white sugar
110 g brown sugar
10 g baking powder
1 g salt
3 eggs
235 ml milk
115 g melted butter
145 g blueberries
170 g peeled and diced fresh peaches

8 g white sugar
2 g ground cinnamon
2 g ground nutmeg
30 g melted butter""",
	instructions="""Preheat the oven to 400 degrees F (200 degrees C). Grease muffin tins, or line with paper liners.
In a large bowl, stir together the flour, 1/2 cup white sugar, brown sugar, baking powder and salt. In a  separate bowl, mix together the eggs, milk  and 1/2 cup of melted butter until well blended. Pour the wet ingredients into the dry, and mix until just blended. Fold in the blueberries and peaches. Fill muffin cups with batter.
Bake for 18 to 20 minutes in the preheated oven, or until the tops spring back when lightly touched. In a small bowl, stir together the remaining sugar, cinnamon and nutmeg. Brush muffins with remaining melted butter, and sprinkle with the cinnamon mixture. Cool in the pan over a wire rack.""",
	)
	r.save()
	r.tags = 'brown_sugar baking_powder salt egg milk butter blueberry peach white_sugar cinnamon nutmeg'

	r = Recipe(
	title="Ferg's Ulster Fry-up",
	ingredients="""2 thick slices Irish bacon
26 g sausages
1 soda bread farl, sliced in half horizontally
2 potato bread farls
15 ml vegetable oil, or as needed
2 slices black pudding
1 tomato, halved
2 eggs""",
	instructions="""Preheat oven to 300 degrees F (150 degrees C).
In a large non-stick skillet over medium heat, cook the bacon and sausages, until they are browned.  Reserving the fat in the pan, transfer to a heat resistant dish. Keep warm in the oven.
Fry both sides of the potato and soda farls in the reserved fat for a few minutes, or until they are golden and crispy. Meanwhile, heat oil in smaller skillet over medium heat and cook black pudding slices and tomato halves. Transfer everything to the dish in the oven to keep warm.
Crack eggs into the pan with any residual bacon grease, adding more oil to the skillet if necessary.  Fry until egg whites are set but yolks are still runny, or to your liking. Divide everything onto 2 separate plates and serve immediately.""",
	)
	r.save()
	r.tags='bacon sausage farl oil black_pudding tomato egg'

if __name__ == "__main__":
    load_data()



















