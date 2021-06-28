import React from 'react';
import Webcam from "react-webcam";

class WebcamCapture extends React.Component {
    constructor(props)
    {
        super(props);
        this.state = {
            image: null,
            videoConstraints: {
                width: 220,
                height: 200,
                facingMode: "user"
            }
        };
    }

    // webcamRef = React.useRef(null);

    // capture = React.useCallback(
    //     () => {
    //     const imageSrc = webcamRef.current.getScreenshot();
    //     },

    //     [webcamRef]
    // );
    capture = async (event) => {}

    render() {
        return (
            <div className="webcam-container">
              <Webcam
                audio={false}
                height={200}
                // ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={220}
                videoConstraints={this.state.videoConstraints}
              />
              <button onClick={(e)=>{ e.preventDefault(); this.capture(); }}>
                Capture
              </button>
            </div>
          )
    }
}

export default WebcamCapture;