! function() {
	function n() {
		u(), t()
	}

	function t() {
		window.addEventListener ? window.addEventListener("message", l, !1) : window.attachEvent("onmessage", l)
	}

	function e(n) {
		var t;
		try {
			t = {}.toString.call(n)
		} catch (e) {
			t = "[object Object]"
		}
		return t
	}

	function r(n) {
		return !!(n && "object" == typeof n && "nodeType" in n && 1 === n.nodeType && n.outerHTML)
	}

	function o(n, t) {
		return n.toLowerCase() < t.toLowerCase() ? -1 : 1
	}

	function c(n) {
		if (null == n) return 1;
		var t, r = e(n);
		if ("[object Number]" === r || "[object Boolean]" === r || "[object String]" === r) return 1;
		if ("[object Function]" === r || "[object global]" === r) return 2;
		if ("[object Object]" === r) {
			var o = Object.keys(n);
			for (t = 0; t < o.length; t++) {
				var c = n[o[t]];
				if ("[object Function]" === (u = {}.toString.call(c)) || "[object Object]" === u || "[object Array]" === u) return 2
			}
			return 1
		}
		if ("[object Array]" === r) {
			for (t = 0; t < n.length; t++) {
				var i = n[t],
					u = {}.toString.call(i);
				if ("[object Function]" === u || "[object Object]" === u || "[object Array]" === u) return 2
			}
			return 1
		}
		return 2
	}

	function i(n, t, r) {
		var c, u, a = "",
			l = [];
		if (r = r || "", t = t || [], null === n) return "null";
		if (void 0 === n) return "undefined";
		if ("[object Object]" == (a = e(n)) && (a = "Object"), "[object Number]" == a) return "" + n;
		if ("[object Boolean]" == a) return n ? "true" : "false";
		if ("[object Function]" == a) return n.toString().split("\n  ").join("\n" + r);
		if ("[object String]" == a) return '"' + n.replace(/"/g, "'") + '"';
		for (u = 0; u < t.length; u++)
			if (n === t[u]) return "[circular " + a.slice(1) + ("outerHTML" in n ? " :\n" + n.outerHTML.split("\n").join("\n" + r) : "");
		if (t.push(n), "[object Array]" == a) {
			for (c = 0; c < n.length; c++) l.push(i(n[c], t));
			return "[" + l.join(", ") + "]"
		}
		if (a.match(/Array/)) return a;
		var f = a + " ",
			s = r + "  ";
		if (r.length / 2 < 2) {
			var b = [];
			try {
				for (c in n) b.push(c)
			} catch (j) {}
			for (b.sort(o), c = 0; c < b.length; c++) try {
				l.push(s + b[c] + ": " + i(n[b[c]], t, s))
			} catch (j) {}
		}
		return l.length ? f + "{\n" + l.join(",\n") + "\n" + r + "}" : f + "{}"
	}

	function u() {
		if (window.console)
			for (var n = 0; n < f.length; n++) ! function() {
				var t = f[n];
				window.console[t] && (window.console[t] = function() {
					for (var n = [].slice.call(arguments), e = [], o = [], u = 0; u < n.length; u++) r(n[u]) ? (o.push(i(n[u].outerHTML)), e.push(1)) : (o.push(i(n[u])), e.push(c(n[u])));
					s.postMessage(["console", {
						"function": t,
						arguments: o,
						complexity: Math.max.apply(null, e)
					}], "*"), this.apply(console, n)
				}.bind(console[t]))
			}()
	}

	function a(n) {
		return !!n.origin.match(/codepen/) && ("object" == typeof n.data && "command" === n.data.type)
	}

	function l(n) {
		if (a(n)) {
			var t = n.data.command;
			try {
				var e = window.eval(t)
			} catch (r) {
				return void console.error(r.message)
			}
			console.log(e)
		}
	}
	var f = ["log", "error", "warn", "info", "debug", "table", "time", "timeEnd", "count", "clear"],
		s = window.parent;
	n()
}();