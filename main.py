from app import app, db
from app.models import User,Location,MotionChange

@app.shell_context_processor
def shell_conext():
    return dict(
        app=app,
        db=db,
        User=User,
        Location=Location,
        MotionChange=MotionChange
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)