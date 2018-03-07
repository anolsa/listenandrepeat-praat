Read from file: "KH5\KH5_kalib3.wav"
soundBase = selected ("Sound")
To TextGrid (silences): 100, 0.0, -15.0, 0.1, 0.1, "", "sounding"
textBase = selected ("TextGrid")
plusObject: soundBase
Extract non-empty intervals: 1, 0

n = numberOfSelected ("Sound")
for i to n
	sound [i] = selected ("Sound", i)
endfor

fileName$ = "\KH5\KH5_kalib3_form.txt"
writeFile: fileName$, ""

for i to n
	selectObject: sound [i]
	dur = Get total duration
	mid = dur/2
	To Formant (burg): 0.0, 5, 5000.0, 0.025, 50.0
	f1 = Get value at time: 1, mid, "Hertz", "Linear"		
	f2 = Get value at time: 2, mid, "Hertz", "Linear"
	appendFileLine: fileName$, fixed$(f1, 0), ",", fixed$(f2, 0)
	Remove
endfor