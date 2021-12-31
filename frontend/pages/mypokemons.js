import React from "react";
import Navbar from "./components/Navbar";

function allpokemons({ mypokemons }) {
    console.log(mypokemons)
    return (
        <div className="container">
            <Navbar />
            <br />
            <h1>My Pokemons</h1>
            <hr />
            <ul className="list-group">
                {mypokemons.map((mypokemon) => (
                    <li class="list-group-item">
                        <input type="checkbox" className="" /> &nbsp;
                        {mypokemon.pokemon_name}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export async function getStaticProps() {
    const object = { email: 'test2@gmail.com' }
    const res = await fetch("http://localhost:8000/get_fav_pokemon", {
        method: 'POST',
        body: JSON.stringify(object)
    })
    const mypokemons = await res.json()
    console.log(mypokemons)


    return {
        props: {
            mypokemons,
        },
    }
}

export default allpokemons