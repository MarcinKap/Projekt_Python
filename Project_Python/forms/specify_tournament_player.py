# # from Project_Python import forms
# #
# #
# # class SpecifyTournamentPlayer(forms.ModelForm):
# #
# #     class Meta:
# #         model =
# #         fields = ('title', 'text',)
# from Project_Python import forms
# from Project_Python.models import PlayerTournament
#
#
# class SpecifyTournamentPlayer(PlayerTournament):
#
#     post = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Write a post...'
#         }
#     ))
#
#     class Meta:
#         model = PlayerTournament
#         fields = ('playertournament',)