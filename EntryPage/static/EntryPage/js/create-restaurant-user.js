        // This example displays an address form, using the autocomplete feature
        // of the Google Places API to help users fill in the information.
        var placeSearch, autocomplete;
        
    var initAutocomplete = function() {
          // Create the autocomplete object, restricting the search to geographical
          // location types.
            //console.log(sessionToken)
          var location_input = document.getElementById('id_PF-restaurant_address')
          var lat = document.getElementById("id_PF-lat")
          var long = document.getElementById("id_PF-long")
          var autocomplete = new google.maps.places.Autocomplete(
              /** @type {!HTMLInputElement} */location_input, lat, long,
              {types: ['geocode'],
            },
            );
          // When the user selects an address from the dropdown, populate the address
          // fields in the form.
          autocomplete.addListener('place_changed', fillInAddress);
          autocomplete.addListener('place_changed',fillInGeolocation);
        }
    
        // [START region_geolocation]
        // Bias the autocomplete object to the user's geographical location,
        // as supplied by the browser's 'navigator.geolocat

    function geolocate() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var geolocation = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          var circle = new google.maps.Circle({
            center: geolocation,
            radius: position.coords.accuracy
          });
          autocomplete.setBounds(circle.getBounds());
        });
      }
    }


function fillInGeolocation(){
  const place = this.getPlace();
  console.log(place)
  document.getElementById("id_PF-long").value= place.geometry.location.lng();
  document.getElementById("id_PF-lat").value= place.geometry.location.lat();

//  for(const component of place.geometry)
 // console.log(document.getElementById("id_PF-geolocation").value)
}
function fillInAddress() {
  // Get the place details from the autocomplete object.
  const place = this.getPlace();
  let address1 = "";
  let postcode = "";

  // Get each component of the address from the place details,
  // and then fill-in the corresponding field on the form.
  // place.address_components are google.maps.GeocoderAddressComponent objects
  // which are documented at http://goo.gle/3l5i5Mr
  for (const component of place.address_components) {
    // @ts-ignore remove once typings fixed
    const componentType = component.types[0];

    switch (componentType) {
      case "street_number": {
        address1 = `${component.long_name} ${address1}`;
        break;
      }

      case "route": {
        address1 += component.short_name;
        break;
      }

      case "postal_code": {
        postcode = `${component.long_name}${postcode}`;
        break;
      }

      case "postal_code_suffix": {
        postcode = `${postcode}-${component.long_name}`;
        break;
      }
      case "locality":
        //document.querySelector("#locality").value = component.long_name;
        locality = component.long_name
        break;
      case "administrative_area_level_1": {
        //document.querySelector("#state").value = component.short_name;
        aalvl1= component.short_name
        break;
      }
      case "country":
        country=component.long_name
        //document.querySelector("#country").value = component.long_name;
        break;
    }
  }
  //document.getElementById("id_PF-geolocation").value= place.geometry.location;
  document.getElementById("id_PF-restaurant_address").value = address1;
  //postalField.value = postcode;
  // After filling the form with address components from the Autocomplete
  // prediction, set cursor focus on the second address line to encourage
  // entry of subpremise information such as apartment, unit, or floor number.
  //address2Field.focus();
}

window.initAutocomplete = initAutocomplete;

function openForm() {
    document.getElementById("myForm").style.display = "block";
}
function closeForm() {
    document.getElementById("myForm").style.display = "none";  
}
