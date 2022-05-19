from flask import Blueprint, render_template, redirect
from app.shipping_form import ShippingForm

new_package = Blueprint("new_package", __name__)

@new_package.route('/', methods=["GET", "POST"])
def new_package():
    form = ShippingForm

    if form.validate_on_submit():
        return redirect('/')

    return render_template('shipping_request.html', form=form)
