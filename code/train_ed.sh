python3 -m model.train  \
                    --batch_size=4 --experiment_name=elmo3 \
                    --training_name=group_global/global_model_12 \
                    --evaluation_minutes=10 --nepoch_no_imprv=6 \
		    --elmo=1 \
                    --span_emb="boundaries"  \
                    --dim_char=50 --hidden_size_char=50 --hidden_size_lstm=150 \
                    --nn_components=pem_lstm \
                    --fast_evaluation=True \
                    --attention_ent_vecs_no_regularization=True --final_score_ffnn=0_0 \
                    --attention_R=10 --attention_K=100 \
                    --train_datasets=aida_train \
                    --ed_datasets=aida_dev_z_aida_test --ed_val_datasets=0 \
                    --global_thr=0.001 --global_score_ffnn=0_0           
