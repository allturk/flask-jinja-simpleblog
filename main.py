from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts=Post()
r_post=posts.return_response()
@app.route('/blog')
def home():
    return render_template("index.html",my_post=r_post)

@app.route('/post/<blog_id>')
def get_post(blog_id):
    return render_template("post.html",blog=r_post,blogid=int(blog_id))

if __name__ == "__main__":
    app.run(debug=True)
