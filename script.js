(function($) {
	setInterval(() => {
		computeTimePositions()
	}, 10);
	let hourhand = $("#hour")
	let minutehand = $("#minute")
	let hourhand1 = $("#hour1")
	let minutehand1 = $("#minute1")

	let h = 0
	let m = 0
	let hpos = 0
	let mpos = 0

	let hTickBox
	let mTickBox
	let hTickNum
	let mTickNum

	function computeTimePositions() {
		let now = new Date()
		let newh = (now.getHours() + 11) % 12 + 1
		let newm = now.getMinutes()
// ---------------------------- Here! You can set the time ----------------------------
		// newh = 10	// hour
		// newm = 30	// minute

		if (newh !== h || newm !== m) {
			console.log('dif')
			h = newh
			m = newm
			hpos = Math.floor(Math.random() * 12) + 1
			do {
				mpos = Math.floor(Math.random() * 12) + 1
			} while (Math.abs(hpos - mpos) < 2)

			refreshFace()
			refreshHands()
		}
	}

	function refreshHands() {
		let degM, degH
		degM = ((mpos * 5 + ((m + 4) % 5) + 1) * 6)
		degH = (hpos * 30) + (30 / 60 * m)

		minutehand.css({
			"transform": "rotate(" + degM + "deg)"
		});
		minutehand1.css({
			"transform": "rotate(" + (degM + 180) + "deg)"
		});
		hourhand.css({
			"transform": "rotate(" + degH + "deg)"
		});
		hourhand1.css({
			"transform": "rotate(" + (degH + 180) + "deg)"
		});
	}

	function refreshFace() {
		if (m === 0) {
			hTickBox.css({
				"transform": "rotate(" + (hpos * 30 - 30) + "deg)"
			})
			hTickNum.css({
				"transform": "rotate(-" + (hpos * 30 - 30) + "deg)"
			})
			if (hpos > 10) {
				hTickNum.css({"left": "-0.5em"})
			}
			hTickNum.text((h + 11) % 12)
		} else {
			hTickBox.css({
				"transform": "rotate(" + (hpos * 30) + "deg)"
			})
			hTickNum.css({
				"transform": "rotate(-" + (hpos * 30) + "deg)"
			})
			if (hpos > 9) {
				hTickNum.css({"left": "-0.5em"})
			}
			hTickNum.text(h)
		}

		mTickBox.css({
			"transform": "rotate(" + (mpos * 30) + "deg)"
		})
		mTickNum.css({
			"transform": "rotate(-" + (mpos * 30) + "deg)"
		})
		if (mpos > 9) {
			mTickNum.css({"left": "-0.5em"})
		}
		mTickNum.text(Math.floor((m + 59) % 60 / 5) * 5)
	}

	function setUpFace() {
		hTickBox = $("<div class=\"faceBox\"></div>")
		hTickNum = $("<div class=\"tickNum\"></div>").text(h).css({
			"transform": "rotate(-" + (hpos * 30) + "deg)"
		});
		hTickNum.css({"left": "-0.5em"})
		hTickBox.append(hTickNum).css({
			"transform": "rotate(" + (hpos * 30) + "deg)"
		})
		$("#clock").append(hTickBox)

		mTickBox = $("<div class=\"faceBox\"></div>")
		mTickNum = $("<div class=\"tickNum\"></div>").text(Math.floor((m + 59) % 60 / 5) * 5).css({
			"transform": "rotate(-" + (mpos * 30) + "deg)"
		});
		mTickNum.css({"left": "-0.5em"})
		mTickBox.append(mTickNum).css({
			"transform": "rotate(" + (mpos * 30) + "deg)"
		})
		$("#clock").append(mTickBox)
	}

	function setSize() {
		var b = $(this) //html, body
		let sz = Math.min(b.width(), b.height())
		let x = Math.floor(sz / 30) - 1
		let px = (x > 25 ? 26 : x) + "px";

		$("#clock").css({
			"font-size": px
		});

		if (b.width() !== 400) {
			setTimeout(function() {
				$("._drag").hide();
			}, 500);
		}
	}

	$(document).ready(function() {
		let now = new Date()
		h = now.getHours()
		m = now.getMinutes()
		hpos = Math.floor(Math.random() * 12) + 1
		do {
			mpos = Math.floor(Math.random() * 12) + 1
		} while (Math.abs(hpos - mpos) < 2)
		setUpFace()
		refreshHands()
		computeTimePositions()
		setSize()
		$(window).resize(function() {
			setSize()
		})
	});
}(jQuery));