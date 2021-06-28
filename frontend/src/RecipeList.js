import React from 'react';
import './RecipeList.css';

class RecipeList extends React.Component {
    constructor(props)
    {
        super(props);
        this.state = {

        };
    }

    render() {
        if (this.props.recipes != null && this.props.recipes) {
            return(
                <ul>
                    {this.props.recipes.map((r, i) => (<li key={i}>{r.recipe.label}</li>))} 
                </ul>
            )
        }
        else {
            return
        }
        
    }
}

export default RecipeList;