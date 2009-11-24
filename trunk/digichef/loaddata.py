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



	r = Recipe(
	title="World's Best Lasagna",
	ingredients="""455 g sweet Italian sausage
340 g lean ground beef
80 g minced onion
2 cloves garlic, crushed
1 (28 ounce) can crushed tomatoes
2 (6 ounce) cans tomato paste
364 g canned tomato sauce
120 ml water
25 g white sugar
1 g dried basil leaves
1 g fennel seeds
2 g Italian seasoning
20 g salt
0.5 g ground black pepper
15 g chopped fresh parsley
12 lasagna noodles
455 g ricotta cheese
1 egg
3 g salt
340 g mozzarella cheese, sliced
60 g grated Parmesan cheese""",
	instructions="""In a Dutch oven, cook sausage, ground beef, onion, and garlic over medium heat until well browned. Stir in crushed tomatoes, tomato paste, tomato sauce, and water. Season with sugar, basil, fennel seeds, Italian seasoning, 1 tablespoon salt, pepper, and 2 tablespoons parsley. Simmer, covered, for about 1 1/2 hours, stirring occasionally.
Bring a large pot of lightly salted water to a boil. Cook lasagna noodles in boiling water for 8 to 10 minutes. Drain noodles, and rinse with cold water.  In a mixing bowl, combine ricotta cheese with egg, remaining parsley, and 1/2 teaspoon salt.
Preheat oven to 375  degrees F (190 degrees C).
To assemble, spread 1 1/2 cups of meat sauce in the bottom of a 9x13 inch baking dish.  Arrange 6 noodles lengthwise over meat sauce. Spread with one half of the ricotta cheese mixture. Top with a third of mozzarella cheese slices. Spoon 1 1/2 cups meat sauce over mozzarella, and sprinkle with 1/4 cup Parmesan cheese.  Repeat layers, and top with remaining mozzarella and Parmesan cheese. Cover with foil: to prevent sticking, either spray foil with cooking spray, or make sure the foil does not touch the cheese.
Bake in preheated oven for 25 minutes. Remove foil, and bake an additional 25 minutes. Cool for 15 minutes before serving.""",
	)
	r.save()
	r.tags='sausage beef onion garlic tomato tomato_paste tomato_sauce water white_sugar basil fennel_seed salt black_pepper parsley pasta ricotta egg mozzarella parmesan'


	r = Recipe(
	title="Apple Pie by Grandma Ople",
	ingredients="""1 recipe pastry for a 9 inch double crust pie
115 g unsalted butter
25 g all-purpose flour
60 ml water
100 g white sugar
110 g packed brown sugar
8 Granny Smith apples - peeled, cored and sliced""",
	instructions="""Preheat oven to 425 degrees F (220 degrees C). Melt the butter in a saucepan. Stir in flour to form a paste. Add water, white sugar and brown sugar, and bring to a boil. Reduce temperature and let simmer.
Place the bottom crust in your pan. Fill with apples, mounded slightly. Cover with a lattice work of crust.  Gently pour the sugar and butter liquid over the crust.  Pour slowly so that it does not run off.
Bake 15 minutes in the preheated oven. Reduce the temperature to 350 degrees F (175 degrees C). Continue baking for 35 to 45 minutes, until apples are soft.""",
	)
	r.save()
	r.tags='pastry butter flour water white_sugar brown_sugar apple'

if __name__ == "__main__":
    load_data()



















