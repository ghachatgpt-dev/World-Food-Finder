import streamlit as st

st.set_page_config(
    page_title="World Meal Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# RECIPE DATABASE
# -----------------------------
RECIPES = [
    {
        "name": "Jollof Rice",
        "country": "Nigeria / West Africa",
        "ingredients": ["rice", "tomatoes", "pepper", "onion", "oil"],
        "time": "45 minutes",
        "description": "A delicious West African rice dish cooked in a rich tomato and pepper sauce.",
        "steps": [
            "Blend the tomatoes, pepper and onion.",
            "Heat oil in a pot and fry the blended mixture.",
            "Add seasoning, salt and a little water.",
            "Wash and add the rice.",
            "Cover and cook until the rice is soft, checking occasionally.",
            "Serve hot with chicken, fish or vegetables."
        ]
    },
    {
        "name": "Fried Rice",
        "country": "China",
        "ingredients": ["rice", "carrot", "peas", "egg", "onion", "oil"],
        "time": "25 minutes",
        "description": "A popular rice dish stir-fried with vegetables and egg.",
        "steps": [
            "Cook the rice and allow it to cool.",
            "Chop the carrots and onions.",
            "Heat a little oil in a frying pan.",
            "Fry the onions and vegetables until tender.",
            "Add the egg and stir until cooked.",
            "Add the rice and seasoning, then stir-fry everything together.",
            "Serve warm."
        ]
    },
    {
        "name": "Pancakes",
        "country": "France",
        "ingredients": ["flour", "milk", "egg", "sugar", "butter"],
        "time": "20 minutes",
        "description": "Soft, golden pancakes that make a lovely breakfast or snack.",
        "steps": [
            "Mix flour, sugar and a pinch of salt in a bowl.",
            "Add milk and eggs.",
            "Whisk until the batter is smooth.",
            "Heat a lightly buttered pan.",
            "Pour a small amount of batter into the pan.",
            "Flip when bubbles appear and cook the other side.",
            "Serve with fruit, honey or your favourite topping."
        ]
    },
    {
        "name": "Spaghetti Bolognese",
        "country": "Italy",
        "ingredients": ["spaghetti", "tomatoes", "onion", "beef", "oil"],
        "time": "40 minutes",
        "description": "Pasta served with a rich tomato and beef sauce.",
        "steps": [
            "Boil the spaghetti according to its packet instructions.",
            "Chop the onions and tomatoes.",
            "Heat oil in a separate pot.",
            "Add the beef and cook until browned.",
            "Add the tomatoes and onions.",
            "Allow the sauce to simmer until cooked.",
            "Serve the sauce over the spaghetti."
        ]
    },
    {
        "name": "Chicken Curry",
        "country": "India",
        "ingredients": ["chicken", "tomatoes", "onion", "garlic", "curry", "oil"],
        "time": "50 minutes",
        "description": "A fragrant and flavourful chicken dish with warming spices.",
        "steps": [
            "Cut the chicken into pieces and season it.",
            "Chop the onions, tomatoes and garlic.",
            "Heat oil and fry the onions until soft.",
            "Add garlic, curry powder and tomatoes.",
            "Add the chicken and stir to coat it in the sauce.",
            "Add a little water, cover and cook until the chicken is thoroughly cooked.",
            "Serve with rice or flatbread."
        ]
    },
    {
        "name": "Tacos",
        "country": "Mexico",
        "ingredients": ["beef", "tomatoes", "onion", "lettuce", "cheese"],
        "time": "30 minutes",
        "description": "Mexican-style tortilla wraps filled with seasoned beef and fresh toppings.",
        "steps": [
            "Cook the beef thoroughly with your preferred seasoning.",
            "Chop the tomatoes, onions and lettuce.",
            "Warm the tortillas according to the packet instructions.",
            "Add the cooked beef to each tortilla.",
            "Top with vegetables and cheese.",
            "Fold and serve."
        ]
    },
    {
        "name": "Vegetable Omelette",
        "country": "International",
        "ingredients": ["egg", "tomatoes", "onion", "pepper", "oil"],
        "time": "15 minutes",
        "description": "A quick and tasty egg dish filled with fresh vegetables.",
        "steps": [
            "Break the eggs into a bowl.",
            "Chop the tomatoes, onions and pepper.",
            "Add the vegetables to the eggs and mix.",
            "Heat a little oil in a frying pan.",
            "Pour in the egg mixture.",
            "Cook until set, turning carefully if needed.",
            "Serve warm."
        ]
    },
    {
        "name": "Shawarma",
        "country": "Middle East",
        "ingredients": ["chicken", "bread", "cabbage", "carrot", "mayonnaise"],
        "time": "35 minutes",
        "description": "A tasty wrap filled with seasoned chicken and crunchy vegetables.",
        "steps": [
            "Cut the chicken into small pieces.",
            "Season and cook the chicken thoroughly.",
            "Slice the cabbage and grate the carrots.",
            "Mix the vegetables with mayonnaise.",
            "Spread the mixture over the flatbread.",
            "Add the cooked chicken.",
            "Roll the bread and serve."
        ]
    },
    {
        "name": "Akara",
        "country": "Nigeria",
        "ingredients": ["beans", "pepper", "onion", "oil"],
        "time": "30 minutes",
        "description": "Traditional Nigerian fried bean cakes with a crisp outside and soft centre.",
        "steps": [
            "Soak the beans and remove their outer skins.",
            "Blend the beans with pepper and onion into a thick batter.",
            "Add salt and mix thoroughly.",
            "Heat oil in a deep frying pan.",
            "Carefully spoon portions of batter into the hot oil.",
            "Fry until golden brown and cooked through.",
            "Drain and serve with pap or bread."
        ]
    },
    {
        "name": "Greek Salad",
        "country": "Greece",
        "ingredients": ["tomatoes", "cucumber", "onion", "cheese", "olive oil"],
        "time": "15 minutes",
        "description": "A refreshing Mediterranean salad made with crisp vegetables and cheese.",
        "steps": [
            "Wash all the vegetables.",
            "Chop the tomatoes and cucumber.",
            "Slice the onions.",
            "Place everything in a bowl.",
            "Add cheese and olive oil.",
            "Mix gently and serve fresh."
        ]
    },
    {
        "name": "Banana Smoothie",
        "country": "International",
        "ingredients": ["banana", "milk", "honey", "yoghurt"],
        "time": "5 minutes",
        "description": "A creamy and refreshing drink made with banana and yoghurt.",
        "steps": [
            "Peel and slice the bananas.",
            "Put the banana pieces into a blender.",
            "Add milk and yoghurt.",
            "Add honey if desired.",
            "Blend until smooth.",
            "Pour into a glass and enjoy."
        ]
    },
    {
        "name": "Potato Fries",
        "country": "Belgium",
        "ingredients": ["potatoes", "salt", "oil"],
        "time": "25 minutes",
        "description": "Golden potato fries with a crisp outside and fluffy centre.",
        "steps": [
            "Wash and peel the potatoes.",
            "Cut them into even strips.",
            "Soak briefly in cold water, then drain and dry.",
            "Heat oil in a suitable pan.",
            "Fry in batches until golden and cooked through.",
            "Drain carefully and season with salt.",
            "Serve hot."
        ]
    }
]

# -----------------------------
# CUSTOM DESIGN
# -----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    .stApp {
        background: #f5f4ee;
        color: #243b32;
        font-family: 'DM Sans', sans-serif;
    }
    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    .hero {
        background: linear-gradient(120deg, #173d34, #286b50);
        padding: 2.5rem 2rem;
        border-radius: 22px;
        color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 5vw, 3.1rem);
        color: white;
        margin: 0;
    }
    .hero p {
        color: #e1eee6;
        font-size: 1.05rem;
        margin-bottom: 0;
    }
    .eyebrow {
        color: #f0c879;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: .75rem;
        margin-bottom: .5rem;
    }
    .section-title {
        font-family: 'Playfair Display', serif;
        color: #193d33;
        font-size: 1.55rem;
        font-weight: 700;
        margin: .5rem 0 1rem;
    }
    .recipe-card {
        background: white;
        border: 1px solid #e5e9e2;
        border-radius: 16px;
        padding: 1.1rem;
        margin-bottom: .8rem;
    }
    .recipe-card h3 {
        color: #193d33;
        font-size: 1.15rem;
        margin: 0 0 .35rem;
    }
    .muted {
        color: #718078;
        font-size: .9rem;
    }
    .match {
        color: #24734f;
        font-weight: 700;
        font-size: .85rem;
    }
    .detail-card {
        background: white;
        border: 1px solid #e5e9e2;
        border-radius: 18px;
        padding: 1.35rem;
    }
    .pill {
        display: inline-block;
        background: #e7f1e9;
        color: #286b50;
        border-radius: 20px;
        padding: .35rem .7rem;
        margin: .2rem .2rem .2rem 0;
        font-size: .83rem;
    }
    div.stButton > button {
        background: #28745c;
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        padding: .55rem 1rem;
    }
    div.stButton > button:hover {
        background: #193d33;
        color: white;
        border: none;
    }
    .footer {
        color: #718078;
        text-align: center;
        padding: 1.5rem 0 .5rem;
        font-size: .85rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">EXPLORE • COOK • ENJOY</div>
    <h1>🌍 World Meal Planner</h1>
    <p>Turn the ingredients in your kitchen into delicious discoveries from around the world.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INGREDIENT SEARCH
# -----------------------------
st.markdown('<div class="section-title">🥕 What is in your kitchen?</div>',
            unsafe_allow_html=True)

st.write("Enter the ingredients you have, separated by commas.")

with st.form("ingredient_form"):
    ingredients_text = st.text_input(
        "Your ingredients",
        placeholder="e.g. rice, tomatoes, onion, pepper",
        key="ingredients_input"
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        search_clicked = st.form_submit_button("🔍 Find my meals", use_container_width=True)
    with col2:
        clear_clicked = st.form_submit_button("✖ Clear", use_container_width=True)

if clear_clicked:
    st.session_state.pop("search_results", None)
    st.rerun()

if search_clicked:
    if not ingredients_text.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        user_ingredients = {
            item.strip().lower()
            for item in ingredients_text.split(",")
            if item.strip()
        }

        results = []
        for recipe in RECIPES:
            recipe_ingredients = set(recipe["ingredients"])
            matches = user_ingredients.intersection(recipe_ingredients)

            if matches:
                score = len(matches) / len(recipe_ingredients) * 100
                results.append({
                    "recipe": recipe,
                    "matches": sorted(matches),
                    "score": score
                })

        results.sort(key=lambda item: item["score"], reverse=True)
        st.session_state["search_results"] = results
        st.session_state["searched_ingredients"] = user_ingredients

# -----------------------------
# RESULTS
# -----------------------------
if "search_results" in st.session_state:
    results = st.session_state["search_results"]

    st.markdown('<div class="section-title">🍽 Your meal suggestions</div>',
                unsafe_allow_html=True)

    if not results:
        st.info("No matching meals found. Try adding different ingredients.")
    else:
        st.success(f"We found {len(results)} possible meal(s) for you!")

        selected_names = [
            item["recipe"]["name"] for item in results
        ]

        left, right = st.columns([1, 1.15], gap="large")

        with left:
            st.markdown("#### Discover your meals")

            for index, item in enumerate(results):
                recipe = item["recipe"]
                with st.container(border=True):
                    st.markdown(f"### 🍲 {recipe['name']}")
                    st.caption(f"📍 {recipe['country']}  ·  ⏱ {recipe['time']}")
                    st.markdown(
                        f'<p class="match">{item["score"]:.0f}% ingredient match</p>',
                        unsafe_allow_html=True
                    )
                    st.write(recipe["description"])
                    st.write("**Ingredients you have:** " +
                             ", ".join(item["matches"]))
                    if st.button(
                        "View full recipe",
                        key=f"recipe_{index}",
                        use_container_width=True
                    ):
                        st.session_state["selected_recipe"] = recipe["name"]
                        st.rerun()

        with right:
            selected = st.session_state.get("selected_recipe")

            if selected not in selected_names:
                selected = selected_names[0]
                st.session_state["selected_recipe"] = selected

            recipe = next(
                item["recipe"] for item in results
                if item["recipe"]["name"] == selected
            )

            st.markdown('<div class="detail-card">', unsafe_allow_html=True)
            st.markdown(f"## 🍴 {recipe['name']}")
            st.markdown(f"**📍 Origin:** {recipe['country']}")
            st.markdown(f"**⏱ Cooking time:** {recipe['time']}")
            st.write(recipe["description"])

            st.markdown("#### 🥕 Ingredients required")
            for ingredient in recipe["ingredients"]:
                st.markdown(
                    f'<span class="pill">{ingredient.title()}</span>',
                    unsafe_allow_html=True
                )

            st.markdown("#### 👩‍🍳 Preparation steps")
            for number, step in enumerate(recipe["steps"], start=1):
                st.markdown(f"**{number}.** {step}")

            st.markdown('</div>', unsafe_allow_html=True)

            st.info(
                "Cooking tip: Check that meat, poultry and eggs are "
                "thoroughly cooked before serving."
            )

else:
    st.markdown('<div class="section-title">✨ How it works</div>',
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🥕 1. Enter ingredients")
        st.write("Tell us what you already have in your kitchen.")

    with col2:
        st.markdown("### 🌍 2. Discover meals")
        st.write("Explore dishes inspired by different countries.")

    with col3:
        st.markdown("### 👩‍🍳 3. Start cooking")
        st.write("Follow simple instructions to prepare your meal.")

    st.markdown("#### Popular food destinations")
    a, b, c, d = st.columns(4)
    a.metric("West Africa", "🇳🇬")
    b.metric("Asia", "🇮🇳")
    c.metric("Europe", "🇮🇹")
    d.metric("Americas", "🇲🇽")

st.markdown("""
<div class="footer">
    WORLD MEAL PLANNER · Explore. Cook. Enjoy. ❤️
    <br>Made with Python and Streamlit
</div>
""", unsafe_allow_html=True)
