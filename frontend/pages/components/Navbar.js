import Link from 'next/link'
export default function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container-fluid">
                <Link href="/">
                    <a className="navbar-brand">My Pokemons</a>
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <Link href="/">
                                <a className="nav-link" aria-current="page" href="/">Home</a>
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link href="/allpokemons">
                                <a className="nav-link">All Pokemons</a>
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link href="/mypokemons">
                                <a className="nav-link">My Pokemons</a>
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link href="/logout">
                                <a className="nav-link">Logout</a>
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}