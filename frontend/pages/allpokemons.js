import React from "react";
import Navbar from "./components/Navbar";

function allpokemons({ pokemons }) {
    return (
        <div className="container">
            <Navbar />
            <br />
            <form>
                <ul className="list-group">
                    {pokemons.map((pokemon) => (
                        <li class="list-group-item">
                            <input type="checkbox" className="" /> &nbsp;
                            {pokemon.name}
                        </li>
                    ))}
                </ul>
                <br />
                <button type="submit" className="btn btn-primary">Add To Favorite</button>
            </form>
        </div>
    );
}

export async function getStaticProps() {
    const res = await fetch("http://localhost:8000/pokemon")
    const pokemons = await res.json()

    return {
        props: {
            pokemons,
        },
    }
}

export default allpokemons