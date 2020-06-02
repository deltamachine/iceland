$(document).ready(function() {
    var slider_words = document.getElementById('slider_words');
    var slider_vars = document.getElementById('slider_vars');
    var slider_texts = document.getElementById('slider_texts');
    var slider_freq =  document.getElementById('slider_freq');

    var min_words_input = document.getElementById('words-min-input');
    var max_words_input = document.getElementById('words-max-input');
    var min_vars_input = document.getElementById('vars-min-input');
    var max_vars_input = document.getElementById('vars-max-input');
    var min_texts_input = document.getElementById('texts-min-input');
    var max_texts_input = document.getElementById('texts-max-input');
    var min_freq_input = document.getElementById('freq-min-input');
    var max_freq_input = document.getElementById('freq-max-input');
	
	noUiSlider.create(slider_words, {
	   start: [2, 5],
	   connect: true,
	   step: 1,
	   orientation: 'horizontal',
	   range: {
	     'min': 1,
	     'max': 10
	   },
	   format: wNumb({
        decimals: 0
       })
	 });

	noUiSlider.create(slider_vars, {
	   start: [2, 5],
	   connect: true,
	   step: 1,
	   orientation: 'horizontal',
	   range: {
	     'min': 1,
	     'max': 10
	   },
	   format: wNumb({
        decimals: 0
       })
	 });

	noUiSlider.create(slider_texts, {
	   start: [1, 20],
	   connect: true,
	   step: 1,
	   orientation: 'horizontal',
	   range: {
	     'min': 1,
	     'max': 49
	   },
	   format: wNumb({
        decimals: 0
       })
	 });

	noUiSlider.create(slider_freq, {
	   start: [2, 5],
	   connect: true,
	   step: 1,
	   orientation: 'horizontal',
	   range: {
	     'min': 1,
	     'max': 10
	   },
	   format: wNumb({
        decimals: 0
       })
	 });

	slider_words.noUiSlider.on('update', function(values, handle) {
	  min_words_input.value = values[0];
	  max_words_input.value = values[1];
	});

	slider_words.noUiSlider.on('update', function(values, handle) {
	  min_vars_input.value = values[0];
	  max_vars_input.value = values[1];
	});

	slider_texts.noUiSlider.on('update', function(values, handle) {
	  min_texts_input.value = values[0];
	  max_texts_input.value = values[1];
	});

	slider_freq.noUiSlider.on('update', function(values, handle) {
	  min_freq_input.value = values[0];
	  max_freq_input.value = values[1];
	});
})
