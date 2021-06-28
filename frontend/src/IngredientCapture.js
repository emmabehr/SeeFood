import React from 'react';
import RecipeList from './RecipeList'
//import WebcamCapture from './WebcamCapture'

class IngredientCapture extends React.Component {
    constructor(props)
    {
        super(props);
        this.state = {
            ingredient_image: null,
            current_ingredient: null,
            current_recipes: null
        };
    }

    updateIngredient = async (event) => {
        this.setState({
            ingredient_image: event.target.files[0]
        })
    }

    submitIngredient = async (event) => {
        event.preventDefault();

        var formData = new FormData();
        formData.append("image", this.state.ingredient_image, this.state.ingredient_image.name);
        console.log(this.state.ingredient_image);
        console.log(formData)
        var data = await fetch(
            "http://localhost:5000/classify/",
            {
                method: "post",
                // headers: { "Content-Type": "multipart/form-data" },
                body: formData,
            }
        );

        const result = await data.json();
        if (result) 
        {
            console.log(result[0])
            var foundIngredient = result[0].ingredient
            this.setState({
                current_ingredient: foundIngredient,
                current_recipes: result[0].recipes
            })
        } 
        else 
        {
            this.setState({
                current_ingredient: null
            })
        }
    }

    // renderWebcamCapture() {
    //     return <WebcamCapture />
    // }
    retry = async() => {
        this.setState({
            ingredient_image: null,
            current_ingredient: null,
            current_recipes: null
        })
    }
    
    renderUploadForm() {
        return (
            <div className="">
                <form onSubmit={this.submitIngredient}>
                    <input type="file" name="image" onChange={this.updateIngredient} accept="image/jpeg"/>
                    <br />
                    <br />
                    <button type="submit" name="upload">
                    Upload
                    </button>
                </form>
            </div>
        );
    }

    renderFoundIngredient() {
        return ([
            <h1>Found Ingredient: {this.state.current_ingredient}</h1>,
            <button type="button" name="retry" onClick={this.retry}>
                    Try Again
            </button>,
            <RecipeList recipes={this.state.current_recipes}/>
        ])
    }

    render() {
        if (this.state.current_ingredient != null) {
            return this.renderFoundIngredient()
        }
        else {
            //return this.renderWebcamCapture()
            return this.renderUploadForm()
        }
    }
}

export default IngredientCapture;