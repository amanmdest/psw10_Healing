consultas_hoje = Consulta.objects.filter(data_aberta__user=request.user
                                          ).filter(data_aberta__data__gte=hoje
                                                   ).filter(data_aberta__data__lt=hoje + timedelta(days=1))

consultas_restantes = Consulta.objects.exclude(id__in=consultas_hoje.values('id')
                                               ).filter(data_aberta__user=request.user)