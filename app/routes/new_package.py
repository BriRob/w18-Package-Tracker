from flask import Blueprint, render_template, redirect
from app.shipping_form import ShippingForm
from app.models import Package, db

np = Blueprint("new_package", __name__, url_prefix='/new_package')

@np.route('/', methods=["GET", "POST"])
def new_package():
    form = ShippingForm()

    if form.validate_on_submit():
        # print(form.data)
        data = form.data
        new_package = Package(sender=data["sender"],
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        new_package.advance_all_locations()
        return redirect('/')

    return render_template('shipping_request.html', form=form)
