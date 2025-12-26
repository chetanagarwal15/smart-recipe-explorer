const API_URL = "https://chetanagarwal15-smart-recipe-explor.vercel.app/";

async function addRecipe() {
    const recipe = {
        name: document.getElementById("name").value,
        ingredients: document.getElementById("ingredients").value.split(","),
        cuisine: document.getElementById("cuisine").value,
        prep_time: Number(document.getElementById("prep_time").value),
        instructions: document.getElementById("instructions").value,
        vegetarian: true
    };

    await fetch(`${API_URL}/recipes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(recipe)
    });

    alert("Recipe added!");
}

async function loadRecipes() {
    const res = await fetch(`${API_URL}/recipes`);
    const data = await res.json();

    const list = document.getElementById("recipeList");
    list.innerHTML = "";

    data.forEach(r => {
        const li = document.createElement("li");
        li.innerText = `${r.name} (${r.cuisine})`;
        list.appendChild(li);
    });
}

async function simplify() {
    const instructions = document.getElementById("aiInput").value;

    const res = await fetch(`${API_URL}/ai/simplify`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ instructions })
    });

    const data = await res.json();
    document.getElementById("aiOutput").innerText = data.simplified;
}
