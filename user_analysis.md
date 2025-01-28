## **Command Line Features:**

***<span style="text-decoration:underline;">“list” Command</span>***

The “list” command allows users to input a category of food, and the command line will output all the types of that category found in the dataset. 

**Example usage:**

	python3 command_line.py --list CHEESE

If a user inputs the general category CHEESE, the command will output the results like:

* CHEESE,BLUE
* CHEESE,BRICK

This command provides a comprehensive list of all types of cheese stored in the dataset.


***<span style="text-decoration:underline;">“healthfacts” Command</span>***

The “healthfacts” command displays nutritional facts for a specific food item.

**Example usage:**

To find information about blue cheese, a user could input:

	python3 command_line.py --healthfacts CHEESE,BLUE

And the output would include nutritional details in categories such as:



* Alpha Carotene
* Beta Carotene
* Carbohydrates
* etc.

This command provides a list of relevant nutritional data.

## **Command Line Potential Users:**

***<span style="text-decoration:underline;">“list”:</span>***

Users who are looking for a specific type of cheese but aren’t sure what it is called in the dataset are able to narrow down their options by first searching the main category CHEESE. This ensures that users won’t have to guess what to input when trying to use the command healthfacts, only to find that their exact food name doesn’t exist in the dataset. Instead, they can search for a keyword and look for the best fit in the dataset. Users could also use this command when seeking recipe substitutes if they are unsure of what similar food types are available to them.

***<span style="text-decoration:underline;">“healthfacts”</span>*:**

Users will use this command when they are looking for detailed nutritional information for a particular food item. This command will give them different kinds of nutritional facts that are valuable to a user who is diet planning, doing academic research, etc. It is also helpful if a user is trying to make health-conscious recipe substitutes, especially used with the list command. A user can go through the types of food listed by the list function to analyze which variety in the food category contains the most of a particular nutrient that they are seeking.

## **Command Line Benefits and Harms as Applied to CIDER:**

***<span style="text-decoration:underline;">Benefits:</span>*** \
	These commands benefit users in a variety of ways. First, the commands provide simple and straightforward access to a helpful data set that users might not otherwise be able to access. Our data set provides users with helpful information about the contents of their food, but it is extremely extensive, which can be overwhelming. The data set is too large to manually search through, thus, by creating these commands, users can access the exact information they need with relative ease.

By providing users access to this data set, we are giving them the opportunity to alter recipes to maximize health benefits as well as be more exploratory in their food choices.

***<span style="text-decoration:underline;">Harms:</span>***

As designers, we are assuming that users are seeking to alter their diet or pay extra attention to it. These very assumptions are built into our culture’s obsession with “clean eating,” dieting, altering food consumption, and overall diet culture. This culture can be helpful for some, but for others, it can be very detrimental to mental health, physical well-being, and overall wellness.

***<span style="text-decoration:underline;">CIDER:</span>***

*Critique:*

Our design assumes that:



* Users have access to a computer
* Users are familiar with Unix/creating a virtual environment/using pandas
* Users have fine motor skills
* Users can interpret and apply our information
* Users can read
* Users can type/spell
* Users have the monetary resources necessary to afford foods and ingredients
* Users are diet conscious/Users are seeking to change their dieting habits
* Users have a space in which they can cook and have the means/ability to cook

*Imagine:*

<span style="text-decoration:underline;">Assumption #1:</span>


One main assumption that excludes users is that these commands are being used to make substitutions in recipes, and by extension, users have the financial luxury to afford substitutions, or to cook expensive foods in general. Oftentimes, fancy substitutions or complicated recipes can be extremely expensive, and thus might not be available to some users. Organic and/or unique foods are significantly more expensive than the basic version of the food, so the substitution-based design might not allow some users to engage with our design.

<span style="text-decoration:underline;">Assumption #2:</span>


Our design's second assumption is that users are familiar with Unix. To run our code, we use a module called pandas. Unfortunately, the latest version of pandas and homebrew don’t work very well together, so in order to operate our commands, users must be in a virtual environment in which pandas is installed. In order to accomplish this, users must be fairly familiar with computers, Unix, and coding, otherwise, they won’t be able to access our commands at all.

<span style="text-decoration:underline;">Assumption #3:</span>


Another assumption that our design makes is that users have a space in which they can cook. Not all users have a kitchen and appliances available, which is necessary to cook a recipe. If we assume that our users are using our design to make recipes, then if users don’t have access to a kitchen, or a stable environment in which to cook, many users likely will not be able to use our commands/have access to our design.

*Design*

<span style="text-decoration:underline;">Assumption #1:</span>


This first assumption hinges on a user’s financial state. To appeal to all users, not just those with substantial financial resources, we could add the command “--cheap” or something similar that accesses a data set about the cheapest version of each ingredient type. For example, this new command might access a data set that stores information about the average price of different kinds of ingredients in different locations. By accessing “CHEESE” with the “--cheap” command, our code would pull from this data set to find the cheapest kind of cheese available, so users could make money-conscious recipe substitutions. This could allow users to use our design, even if they aren’t able to make expensive substitutions.

<span style="text-decoration:underline;">Assumption #2:</span>


The only reasonable redesign to make our code more available to users without significant Unix experience would be to alter our code to use another module that is more compatible with Homebrew. By doing this, users could use basic commands in Terminal to run our code, rather than having to also create a virtual environment and install pandas. Thus, even if users aren’t Unix experts, they could likely still use our simplest commands.

<span style="text-decoration:underline;">Assumption #3:</span>


It is difficult to fix this assumption because the assumption is embedded in the use of the design. Our model and website are both designed with cooking in mind. If users can’t cook or don’t have the resources to cook, then this design is essentially worthless to them. However, in this case, I don’t think that there is a viable solution. The very need for our design is for cooking, so, it can’t likely be redesigned in a way to include users who don’t plan on cooking. This illustrates that in some cases, some designs are designed for a specific group of users, and they can’t be modified to include all users (i.e. the universal design is limited, and thus can not *truly* be made universal).
