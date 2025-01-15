from django import forms

class SurveyForm(forms.Form):
    name = forms.CharField(
    label="नाम",
    max_length=100,
    widget=forms.TextInput(attrs={"placeholder": "अपना पूरा नाम दर्ज करें"}),
    )
    number = forms.CharField(
        label="फोन नंबर",
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "अपना फोन नंबर दर्ज करें"}),
    )
    email = forms.EmailField(
        label="ईमेल",
        widget=forms.EmailInput(attrs={"placeholder": "अपना ईमेल पता दर्ज करें"}),
    )
    unit = forms.CharField(
        label="यूनिट (वैकल्पिक)",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "यूनिट दर्ज करें (यदि लागू हो)"}),
    )
    CHOICES = [
        (0, "0 - बिल्कुल नहीं"),
        (1, "1 - कभी-कभी"),
        (2, "2 - अक्सर"),
        (3, "3 - लगभग हमेशा"),
    ]

    Q1 = forms.ChoiceField(
    choices=CHOICES,
    label="1. मुझे आराम करने में मुश्किल हो रही थी",
    widget=forms.RadioSelect,
    )
    Q2 = forms.ChoiceField(
        choices=CHOICES,
        label="2. मेरे शुष्क मुँह की मुझे जानकारी थी",
        widget=forms.RadioSelect,
    )
    Q3 = forms.ChoiceField(
        choices=CHOICES,
        label="3. मैं कोई भी सकारात्मक भावना को महसूस नहीं कर पा रहा था",
        widget=forms.RadioSelect,
    )
    Q4 = forms.ChoiceField(
        choices=CHOICES,
        label="4. मुझे सांस लेने में कठिनाई का अनुभव हुआ (जैसे, अत्यधिक तेजी से सांस लेना, शारीरिक परिश्रम के अभाव में सांस का फूलना)",
        widget=forms.RadioSelect,
    )
    Q5 = forms.ChoiceField(
        choices=CHOICES,
        label="5. मुझे चीजों की शुरुआत करने में कठिनाई हुई",
        widget=forms.RadioSelect,
    )
    Q6 = forms.ChoiceField(
        choices=CHOICES,
        label="6. मैं परिस्थितियों पर अधिक प्रतिक्रिया करने के लिए प्रवृत्त हुआ",
        widget=forms.RadioSelect,
    )
    Q7 = forms.ChoiceField(
        choices=CHOICES,
        label="7. मुझे कम्पन का अनुभव हुआ (जैसे, हाथों में)",
        widget=forms.RadioSelect,
    )
    Q8 = forms.ChoiceField(
        choices=CHOICES,
        label="8. मुझे लगा कि मैं बहुत अधिक तंत्रिका ऊर्जा (नर्वस एनर्जी) का उपयोग कर रहा था",
        widget=forms.RadioSelect,
    )
    Q9 = forms.ChoiceField(
        choices=CHOICES,
        label="9. मैं उन स्थितियों के बारे में चिंतित था जिनमें मैं घिरा सकता था और खुद को मूर्ख बना सकता था",
        widget=forms.RadioSelect,
    )
    Q10 = forms.ChoiceField(
        choices=CHOICES,
        label="10. मुझे लगा कि मेरे पास आगे देखने की कोई उम्मीद नहीं है",
        widget=forms.RadioSelect,
    )
    Q11 = forms.ChoiceField(
        choices=CHOICES,
        label="11. मैंने अपने आप को व्यथित पाया",
        widget=forms.RadioSelect,
    )
    Q12 = forms.ChoiceField(
        choices=CHOICES,
        label="12. मुझे आराम करना मुश्किल लगा",
        widget=forms.RadioSelect,
    )
    Q13 = forms.ChoiceField(
        choices=CHOICES,
        label="13. मैं उदास और निराश महसूस कर रहा था",
        widget=forms.RadioSelect,
    )
    Q14 = forms.ChoiceField(
        choices=CHOICES,
        label="14. मैं जो कुछ कर रहा था उसमें बाधा रूप कुछ भी चीज के प्रति असहिष्णु था",
        widget=forms.RadioSelect,
    )
    Q15 = forms.ChoiceField(
        choices=CHOICES,
        label="15. मुझे लगा कि मैं दहशत के करीब था",
        widget=forms.RadioSelect,
    )
    Q16 = forms.ChoiceField(
        choices=CHOICES,
        label="16. मैं किसी भी चीज को लेकर उत्साहित नहीं हो पा रहा था",
        widget=forms.RadioSelect,
    )
    Q17 = forms.ChoiceField(
        choices=CHOICES,
        label="17. मुझे लगा कि मैं एक व्यक्ति के रूप में ज्यादा लायक नहीं था",
        widget=forms.RadioSelect,
    )
    Q18 = forms.ChoiceField(
        choices=CHOICES,
        label="18. मुझे लगा कि मैं यूं ही अतिभावुक था",
        widget=forms.RadioSelect,
    )
    Q19 = forms.ChoiceField(
        choices=CHOICES,
        label="19. मैं शारीरिक परिश्रम के अभाव में अपने हृदय की क्रिया से अवगत था (उदाहरण के लिए, हृदय गति में वृद्धि की भावना, हृदय की धड़कन का छूटना)",
        widget=forms.RadioSelect,
    )
    Q20 = forms.ChoiceField(
        choices=CHOICES,
        label="20. मुझे बिना किसी उचित कारण के डर लग रहा था",
        widget=forms.RadioSelect,
    )
    Q21 = forms.ChoiceField(
        choices=CHOICES,
        label="21. मुझे लगा कि जीवन व्यर्थ था",
        widget=forms.RadioSelect,
    )
