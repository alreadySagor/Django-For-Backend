from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction

from . forms import DepositeForm, WithdrawForm, LoanRequestForm
from constants import DEPOSITE, WITHDRAWAL, LOAN, LOAN_PAID
from django.contrib import messages
# Create your views here.

# ei view ke inherit kore amra deposite, withdraw, loan request er kaj korbo
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = ''
    model = Transaction
    title = ''
    success_url = ''

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account,
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })

class DepositeMoneyView(TransactionCreateMixin):
    form_class = DepositeForm
    title = 'Deposte'

    def get_initial(self):
        initial = {'transaction_type' : DEPOSITE}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']  
        )
        messages.success(self.request, f'{amount}$ was deposited to your account successfully')
        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type' : WITHDRAWAL}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance -= amount
        account.save(
            update_fields = ['balance']
        )
        messages.success(self.request, f"Successfully withdrawn {amount}$ from your account")
        return super().form_valid(form)

class LoanRequestView(Transaction):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transaction_type' : LOAN}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account = self.request.user.account, transaction_type = 3, loan_approve = True).count() # 3 means LOAN jeta constants er moddhe bole deya ache. 3 er bodole LOAN dileu hoto
        if current_loan_count >= 3:
            return HttpResponse("You have crossed your limits")
        messages.success(self.request, f"Loan request for amount {amount}$ has been successfully sent to admin")
        return super().form_valid(form)
    