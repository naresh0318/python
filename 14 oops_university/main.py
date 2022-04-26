from batch.batch import Batch
from university.attainu import Attainu

if __name__ == '__main__':
        attainu = Attainu("attinu", "Noida-20", "A" )
        
        subramanyam = Batch("subramanyam", 100)
        attainu.add_batch(subramanyam)

        cv_raman = Batch("cv_raman", 80)
        attainu.add_batch(cv_raman)

        aryabhatta = Batch("aryabhatta", 100)
        attainu.add_batch(aryabhatta)

        attainu.print_all_batches()
