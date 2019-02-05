import React from 'react';
import { Route } from 'react-router-dom';

import Home from './Home';
import About from './About';
import Work from './Work';
import Service from './Service';
import Contact from './Contact';


class Body extends React.Component {

    render() {
        return (
            <div>
                <Route exact path={process.env.PUBLIC_URL + '/'} component={Home} />
                <Route exact path={process.env.PUBLIC_URL + '/work'} component={Work} />
                <Route exact path={process.env.PUBLIC_URL + '/services'} component={Service} />
                <Route exact path={process.env.PUBLIC_URL + '/about'} component={About} />
                <Route exact path={process.env.PUBLIC_URL + '/contact'} component={Contact} />
            </div>
        )
    }
}

export default Body;