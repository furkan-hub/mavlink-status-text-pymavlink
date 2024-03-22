yer kotnrol istasyonu ve görev bilgisayarının haberleşmesi için mavlink ağı sayesinde otopilot üzerinden haberleşme scriptidir.
aşağıdaki şemada bağlantısı verilmiştir.

![mav2](https://github.com/furkan-hub/mav-test/assets/72547366/b94bf200-bd95-48fc-805e-86cddd59973a)

bu haberleşmenin çalışması için iki bağlantıdan birisinin master olması gerekiyor ya alan master olacak yada gönderen iki slave birbiri arasında veri alışverişi yapamıyor.

mavproxy de port çoğaltma sayesinde hem mission plannera hem de koduna bağlanabilirsin gerekirse mission planeri iptal edebilirsin.

fakat şunu unutmayın mavrpoxyden çoğaltılan portlar UDP olmak zorunda.

jetsondan bağlanmak için ama buna gerek yok

```
mavproxy.py --master=/dev/ttyACM0 
```

jetsona ssh bağlantısı için ip

```
ssh aisoft@192.168.1.107 
```

mavproxy den port çoğaltmak için gerekli komut

```
mavproxy.py --out 127.0.0.1:5760 --out 127.0.0.1:5762
```

